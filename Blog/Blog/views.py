
from django.shortcuts import render, redirect
from .models import Blog, BlogArticle
from .forms import BlogForm, BlogArticleForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.
def index(request):
    """主页"""
    return render(request, 'Blog/index.html')


@login_required
def blogs(request):
    """显示所有主题"""
    blogs = Blog.objects.filter(owner=request.user).order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'Blog/Blogs.html', context)


@login_required
def blog(request, blog_id):
    """显示单个主题及其所有的条目"""
    blog = Blog.objects.get(id=blog_id)
    # 确认请求的主题属于当前用户
    if blog.owner != request.user:
        raise Http404
    ba = blog.blogarticle_set.order_by('-date_added')
    context = {'blog': blog, 'blogarticles': ba}
    return render(request, 'Blog/Blog.html', context)


@login_required
def new_blog(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = BlogForm()
    else:
        # POST提交的数据：对数据进行处理
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('Blog:blogs')
    context = {'form': form}
    return render(request, 'Blog/new_Blog.html', context)


@login_required
def new_blogarticle(request, blog_id):
    """在特定的主题中添加新条目"""
    blog = Blog.objects.get(id=blog_id)
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = BlogArticleForm()
    else:
        # POST提交的数据：对数据进行处理
        form = BlogArticleForm(data=request.POST)
        if form.is_valid():
            new_blogarticle = form.save(commit=False)
            new_blogarticle.blog = blog
            new_blogarticle.save()
            return redirect('Blog:blog', blog_id=blog_id)
    context = {'blog': blog, 'form': form}
    return render(request, 'Blog/new_BlogArticle.html', context)


@login_required
def edit_blogarticle(request, ba_id):
    """编辑既有的条目"""
    ba = BlogArticle.objects.get(id=ba_id)
    blog = ba.blog
    # 确认请求的主题属于当前用户
    if blog.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求：使用当前的条目填充表单
        form = BlogArticleForm(instance=ba)
    else:
        # POST提交的数据：对数据进行处理
        form = BlogArticleForm(instance=ba, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Blog:blog', blog_id=blog.id)
    context = {'blogarticle': ba, 'blog': blog, 'form': form}
    return render(request, 'Blog/edit_BlogArticle.html', context)
