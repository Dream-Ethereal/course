"""定义Blog的URL模式"""
from django.urls import path
from . import views

app_name = 'Blog'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有主题的页面
    path('Blogs/', views.blogs, name='blogs'),
    # 特定主题的详细页面
    path('Blogs/<int:blog_id>/', views.blog, name='blog'),
    # 用于添加新主题的网页
    path('new_Blog/', views.new_blog, name='new_blog'),
    # 用于添加新条目的网页
    path('new_BlogArticle/<int:blog_id>/', views.new_blogarticle, name='new_blogarticle'),
    # 用于编辑条目的页面
    path('edit_BlogArticle/<int:ba_id>/', views.edit_blogarticle, name='edit_blogarticle'),
]
