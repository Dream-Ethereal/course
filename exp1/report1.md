# 实验一 Git和Markdown基础

班级： 21计科1

学号： B20210302129

姓名： 吴俊君

Github地址：<https://github.com/TYRandall/course>

---

## 实验目的

1. Git基础，使用Git进行版本控制
2. Markdown基础，使用Markdown进行文档编辑

## 实验环境

1. Git
2. VSCode
3. VSCode插件

## 实验内容和步骤

### 第一部分 实验环境的安装

1. 安装git，从git官网下载后直接点击可以安装：[git官网地址](https://git-scm.com/)
2. 从Github克隆课程的仓库：[课程的仓库地址](https://github.com/zhoujing204/python_course)，运行git bash应用（该应用包含在git安装包内），在命令行输入下面的命令（命令运行成功后，课程仓库会默认存放在Windows的用户文件夹下）

```bash
git clone https://github.com/zhoujing204/python_course.git
```

如果你在使用`git clone`命令时遇到SSL错误，请运行下面的git命令(这里假设你的Git使用了默认安装目录)：

```bash
git config --global http.sslCAInfo "C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt"
```

或者运行下面的命令:

```bash
git config --global http.sslVerify false
```

如果遇到错误：`error setting certificate file`，请运行下面的命令重新指定git的安全证书：

```bash
git config --global --unset http.sslCAInfo
git config --global http.sslCAInfo "C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt"
```

该仓库的课程材料后续会有更新，如果需要更新课程材料，可以在本地课程仓库的目录下运行下面的命令：

```bash
git pull
```

在本地的仓库内容有更新后，可以运行下面的命令，将本地仓库的内容和远程仓库的内容同步：

```bash
git push origin main
```

3. 注册Github账号或者Gitee帐号，创建一个新的仓库，使用上面同样的方法将该仓库clone到本地，用于存放实验报告和实验代码，使用`git pull`和`git push`命令保持远程仓库和本地仓库的同步。
4. 安装VScode，下载地址：[Visual Studio Code](https://code.visualstudio.com/)
5. 安装下列VScode插件
   - GitLens
   - Git Graph
   - Git History
   - Markdown All in One
   - Markdown Preview Enhanced
   - Markdown PDF
   - Auto-Open Markdown Preview
   - Paste Image
   - markdownlint

### 第二部分 Git基础

教材《Python编程从入门到实践》P440附录D：使用Git进行版本控制，按照教材的步骤，完成Git基础的学习。

### 第三部分 learngitbranching.js.org

访问[learngitbranching.js.org](https://learngitbranching.js.org)，如下图所示完成Main部分的Introduction Sequence和Ramping Up两个小节的学习。

![Learngitbranching.js.org](/Experiments/img/2023-07-28-21-07-40.png)

上面你学习到的git命令基本上可以应付百分之九十以上的日常使用，如果你想继续深入学习git，可以：

- 继续学习[learngitbranching.js.org](https://learngitbranching.js.org)后面的几个小节（包括Main和Remote）
- 在日常的开发中使用git来管理你的代码和文档，用得越多，记得越牢
- 在git使用过程中，如果遇到任何问题，例如：错误删除了某个分支、从错误的分支拉取了内容等等，请查询[git-flight-rules](https://github.com/k88hudson/git-flight-rules)

### 第四部分 Markdown基础

查看[Markdown cheat-sheet](http://www.markdownguide.org/cheat-sheet)，学习Markdown的基础语法

使用Markdown编辑器（例如VScode）编写本次实验的实验报告，包括[实验过程与结果](#实验过程与结果)、[实验考查](#实验考查)和[实验总结](#实验总结)，并将其导出为 **PDF格式** 来提交。

如何将markdown文件转换为pdf格式的文件？

- 安装vscode插件Markdown PDF，安装后重启vscode，打开markdown文件，按下`Ctrl+Shift+P`，输入`Markdown PDF: Export (pdf)`，回车即可导出pdf文件。
- 使用Google Chrome浏览器，在Github网站或者Gitee网站打开你的仓库，浏览你的markdown文件，按下`Ctrl+P`，选择`打印`，选择`目标打印机`为`另存为PDF`，点击`保存`即可导出pdf文件。

## 实验过程与结果

### 一、建立Github仓库

进入Github官网，登录自己的个人账号，在右上角选择 New repository，自定义名称，新建仓库。

### 二、配置SSH、绑定Github账号

在上传文件前还需配置自己的SSH，在GitBash中输入以下指令：

```bash
ssh-keygen -t rsa -C "YourEmail"
```

输入完基本全程回车即可。

生成成功后，去对应目录C:\Users\YourName\ .ssh里用记事本打开id_rsa.pub，得到ssh key公钥，复制粘贴进Github中的"Settings" -> "SSH and GPG keys" -> "New SSH key"。

可以用以下指令验证，输出"Hi"就是配置成功：

```bash
ssh -T git@github.com
```

其次，输入以下指令进行绑定自己的Github：

```bash
git config --global user.name "github的用户名"
git config --global user.email "登录github的邮箱"
```

### 三、上传本地文件至仓库

1. 在本地新建一个要上传的文件所在的文件夹，例如 course/ ，在这个文件夹里新建一个report1.md文件，该文件用于保存Python实验课程的实验报告一的内容。
2. 对 course 文件夹进行右键，选择 "Open Git Bash here"。
3. 分别输入以下指令

```bash
git init
```

该命令可以将当前文件夹初始化为一个Git可以管理的仓库

```bash
git add .
```

该命令可以将当前文件夹下所有的文件夹添加到缓冲区

```bash
git commit -m "first commit"
```

该命令可以将缓冲区里的文件提交到本地仓库

```bash
git remote add origin git@github.com:yourname/yourRepository_name.git
```

该命令可以关联远程仓库

```bash
git push -u origin master
```

该命令可以将本地库的文件提交进远程仓库

执行完后，可以再次打开自己的仓库就可以看见刚刚自己提交的文件。

## 实验考查

请使用自己的语言回答下面的问题，这些问题将在实验检查时用于提问和答辩，并要求进行实际的操作。

1. 什么是版本控制？使用Git作为版本控制软件有什么优点？
   1. 版本控制可以在开发过程中，对一个项目的操作历史记录进行记录，方便开发人员进行查看，也可以备份历史记录，来进行回溯。
   2. Git能够支持多人进行并行开发同一个项目，并且可以不受版本限制。操作也具有便捷性，只需要在本地就可以将文件上传至远程仓库。

2. 如何使用Git撤销还没有Commit的修改？如何使用Git检出（Checkout）以前的Commit？（实际操作）

    ```bash
    #撤销还没提交的修改
    git restore <文件路径>
    ```

    ```bash
    #列出以前的所有的提交，用来找到目标commit的哈希值
    git log
    #检出以前的提交
    git checkout <要检出的提交的哈希值或者引用名称>
    ```

3. Git中的HEAD是什么？如何让HEAD处于detached HEAD状态？（实际操作）

   HEAD是一个指针，它指向当前所在的分支。可以通过以下指令将切换到指定的某一次提交，使得HEAD处于detached HEAD状态：

   ```bash
   git checkout <commit id>
   ```

4. 什么是分支（Branch）？如何创建分支？如何切换分支？（实际操作）

    1. 分支可以简单地理解为一条独立的开发线，允许开发者在同一时间内对代码进行多个版本的开发和迭代。
    2. 通过以下指令可以创建分支：

    ```bash
    #创建新的分支newBranch，并将HEAD指向该分支
    git checkout -b newBranch
    ```

    3. 通过以下指令可以切换分支：

    ```bash
    #切换到master分支上
    git checkout master
    ```

5. 如何合并分支？git merge和git rebase的区别在哪里？（实际操作）

    1. git merge：这个命令用于将指定分支合并到当前分支。例如，如果你有一个名为“dev”的分支，并且你想将它合并到你的主分支“master”，你可以运行以下命令：

    ```bash
    git checkout master  
    git merge dev
    ```

    这个命令将会把“dev”分支的所有更改合并到“master”分支。

    2. git rebase：这个命令也可以用于将指定分支合并到当前分支。使用这个命令时，你需要切换到你想要合并的分支（比如“dev”），然后运行以下命令：

    ```bash
    git checkout dev  
    git rebase master
    ```

    这个命令将会把“master”分支的所有更改应用到“dev”分支上。

    3. git rebase 可以保留所有的分支提交，并且在合并时保留清晰的提交历史；git merge 合并分支时会形成一个新的提交，不保留所有的分支提交。

6. 如何在Markdown格式的文本中使用标题、数字列表、无序列表和超链接？（实际操作）
   
   1. 标题
   
        ```markdown
        # 一级标题
        ## 二级标题
        ### 三级标题
        #### 四级标题
        ##### 五级标题
        ```

        效果如下：
        # 一级标题
        ## 二级标题
        ### 三级标题
        #### 四级标题
        ##### 五级标题

   2. 数字列表
   
        ```markdown
        1. 项目1
        2. 项目2
        3. 项目3
        ```

        效果如下：

        1. 项目1
        2. 项目2
        3. 项目3


   3. 无序列表
   
        ```markdown
        - 项目1
        - 项目2
        - 项目3
        ```

        或者

        ```markdown
        * 项目1
        * 项目2
        * 项目3
        ```

        效果如下：
        - 项目1
        - 项目2
        - 项目3

   4. 超链接
      
        ```markdown
        这是一个链接到<https://github.com/TYRandall>的文本。
        ```
        
        或者

        ```markdown
        这是一个链接到[我的Github](https://github.com/TYRandall)的文本。
        ```

        效果如下：

        这是一个链接到<https://github.com/TYRandall>的文本。

        这是一个链接到[我的Github](https://www.example.com)的文本。



## 实验总结

经过第一次的Python实验课，我接触到了Github的使用，学习到了如何利用Git建立本地仓库，并且通过本地仓库上传至远程仓库，见识到了Git作为一个版本控制工具的强大，可以通过本地快速便捷的上传文件至项目。也学习到了很多关于Git的命令，例如git commit和git checkout等等，通过以游戏闯关的方式进行了Git命令的学习，能够更加的以玩促学，以达到更加的熟悉命令的目的，这为我们后续的课程的进行打下了基础。还学习了Markdown的简单语法应用，包括各级标题、数字列表、无序列表、超链接的语法书写，便于课程的实验报告的书写，使其变得美观、整齐。
