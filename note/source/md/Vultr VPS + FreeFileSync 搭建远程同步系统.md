[//]: # (20180711)
# Vultr VPS + FreeFileSync 搭建远程同步系统
本文主要介绍通过Vultr VPS作为服务器配合软件FreeFileSync的sftp功能搭建远程同步系统。其基本原理为通过sshfs将服务器上的文件夹映射到本地文件夹，在用FreeFileSync进行文件夹内容的比较与同步。
这里假设你已经购买Vultr虚拟服务器并成功部署，如果需要详细购买流程可以参考[这篇文章](https://blog.csdn.net/sinat_32829963/article/details/79261297)。本文搭建VPS用的系统是Ubuntu 16.04 x64， 下面从ssh登录VPS开始，以LinuxMint 18.3为例。

### 通过ssh登录VPS
假设VPS的IP为2.2.2.2，密码为rootpw。终端输入：

``` bash
ssh root@2.2.2.2
```

接下来输入密码rootpw。于是进入了VPS：

``` bash
root@vultr:~#
```

此时默认所在位置位于/root。

##### 创建新的管理员账户
默认账户是root账户，权限比较大，命令输错危害比较大。出于安全性考虑同时避免输入默认的乱码作为密码，建立一个新的管理员帐号十分有必要。
如果locale命令报错`Cannot set LC_ALL to default locale: No such file or directory`，输入命令`export LC_ALL=en_US.UTF-8`。
假设新帐号名字为newusr，密码为newpw， 输入命令`adduser newusr`，并根据提示完善帐号信息：

``` text
root@vultr:~# adduser newusr
Adding user `newusr' ...
Adding new group `newusr' (1001) ...
Adding new user `newusr' (1001) with group `newusr' ...
Creating home directory `/home/newusr' ...
Copying files from `/etc/skel' ...
New password: 
Retype new password: 
passwd: password updated successfully
Changing the user information for newusr
Enter the new value, or press ENTER for the default
	Full Name []: 
	Room Number []: 
	Work Phone []: 
	Home Phone []: 
	Other []: 
Is the information correct? [Y/n] y
```

此时建立的帐号是普通帐号，没有执行sudo的权限，需要通过以下步骤添加管理员权限：

``` bash
root@vultr:~# visudo
```

将里面`# User privilege specification`下添加`newusr  ALL=(ALL:ALL) ALL`：

``` python
# User privilege specification
root    ALL=(ALL:ALL) ALL
newusr  ALL=(ALL:ALL) ALL
```

然后Ctrl+O保存(还需要按一次Enter确定), Ctrl+X退出。
输入`exit`退出VPS登录。

##### 登录VPS建立远程同步文件夹
假设要建立的目录为/home/newusr/Sync/:

``` text
ssh newusr@2.2.2.2
newusr@2.2.2.2's password: 
```

``` bash
mkdir Sync
```

##### 安装并设置sshfs
假设本地待映射文件夹路径为$localdir，其大概长得类似这样: /home/XXX/Document/folder，最好不需要管理员权限就可以对其进行操作。
安装sshfs:

``` bash
sudo aptitude install sshfs
```

下面要把远程VPS上的文件夹映射到本地文件夹(注意冒号后不要有空格):

``` bash
sshfs ssh newusr@2.2.2.2:/home/newusr/Sync/ $localdir
```

之后就可以用FreeFileSync通过同步本地两个文件夹来实现本地文件夹与VPS文件夹的同步了。

最后是终止映射:

``` bash
fusermount -u $localdir
```

##### 参考链接:
[Vultr VPS搭建SS(ShadowSocks)教程](https://blog.csdn.net/sinat_32829963/article/details/79261297)

[Ubuntu16.04系统中创建新用户](https://blog.csdn.net/timothy93bp/article/details/77679000)

[FreeFileSync User Manual](https://freefilesync.org/manual.php?topic=ftp-setup)

[使用 SSHFS 挂载远程的 Linux 文件系统及目录](https://www.linuxprobe.com/sshfs-linux-fires.html)
