[//]: # (20180714)
[//]: # (msys2是一个GNU出品的windows下最小Linux环境, 可以运行很多Linux程序。本文介绍其安装后的配置过程。)
# msys2配置

这里假设你已经成功安装[msys2](https://www.msys2.org/), 并且安装目录为`$directory`, 比如说长这个样子: `C:\ProgramFiles\msys64`。

### 改变软件源
安装好msys后的第一件事是改变软件源, 否则直接连官方服务器速度感人。这里推荐中国科学技术大学的软件源(ustc)。

+ 用记事本打开`$directory\etc\pacman.d\mirrorlist.msys`, 把ustc源加到第一行:
``` text
## Primary
## msys2.org
Server = http://mirrors.ustc.edu.cn/msys2/msys/$arch/
Server = http://repo.msys2.org/msys/$arch
Server = https://downloads.sourceforge.net/project/msys2/REPOS/MSYS2/$arch
Server = http://www2.futureware.at/~nickoe/msys2-mirror/msys/$arch/
```

+ 用记事本打开`$directory\etc\pacman.d\mirrorlist.mingw32`, 把ustc源加到第一行:
``` text
## Primary
## msys2.org
Server = http://mirrors.ustc.edu.cn/msys2/mingw/i686/
Server = http://repo.msys2.org/mingw/i686
Server = https://downloads.sourceforge.net/project/msys2/REPOS/MINGW/i686
Server = http://www2.futureware.at/~nickoe/msys2-mirror/mingw/i686
```

+ 用记事本打开`$directory\etc\pacman.d\mirrorlist.mingw64`, 把ustc源加到第一行:
``` text
## Primary
## msys2.org
Server = http://mirrors.ustc.edu.cn/msys2/mingw/x86_64
Server = http://repo.msys2.org/mingw/x86_64
Server = https://downloads.sourceforge.net/project/msys2/REPOS/MINGW/x86_64
Server = http://www2.futureware.at/~nickoe/msys2-mirror/mingw/x86_64
```

### 用pacman更新系统以及安装软件
msys2用pacman管理软件, 和archlinux是一样的。pacman常用命令:

``` bash
pacman -Syu       # 同步软件库并更新系统到最新状态 
pacman -Ss vim    # 搜索软件仓库里名字含有vim的软件包
pacman -S git     # 安装git
pacman -R git     # 删除git
```

### 添加右键命令"msys here"
以windows 10为例。

1 找到msys2的安装目录`$directory`, 新建`msys2.bat`, 内容如下(将`$directory`换成自己的路径):

``` text
$directory\msys2_shell.cmd -mingw64 -where %cd%
```

2 `Win + r`启动regedit, 进入`HKEY_CLASSES_ROOT\Directory\Background\shell`, 新建**项**, 命名为`msys2`(和cmd、Powershell同一等级)。

3 右键msys2, 再新建**项**, 命名为`command`。选中新建的`command`, 更改右边窗口的值为`$directory\msys2.bat`

4 右键msys2, 新建**字符串**, 名称为icon, 值为`$directory\msys2.ico`

在这个过程中, `msys2`项使系统识别了在右键菜单中要添加名为`msys2`的选项, `command`项添加指出关联的程序位置, `icon`字符串指向要用的图标地址。

参考文章:

[给 MSYS2 添加中科大的源](https://blog.csdn.net/liyuanbhu/article/details/56496501)

[pacman常用命令](https://www.2cto.com/kf/201704/620094.html)

[为msys2添加右键，在当前目录打开](https://blog.csdn.net/u011924787/article/details/69485944)
