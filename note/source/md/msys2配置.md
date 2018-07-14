[//]: # (20180714)
# msys2����

����������Ѿ��ɹ���װ[msys2](https://www.msys2.org/), ���Ұ�װĿ¼Ϊ`$directory`, ����˵���������: `C:\ProgramFiles\msys64`��

### �ı����Դ
��װ��msys��ĵ�һ�����Ǹı����Դ, ����ֱ�����ٷ��������ٶȸ��ˡ������Ƽ��й���ѧ������ѧ�����Դ(ustc)��

+ �ü��±���`$directory\etc\pacman.d\mirrorlist.msys`, ��ustcԴ�ӵ���һ��:
``` python
## Primary
## msys2.org
Server = http://mirrors.ustc.edu.cn/msys2/msys/$arch/
Server = http://repo.msys2.org/msys/$arch
Server = https://downloads.sourceforge.net/project/msys2/REPOS/MSYS2/$arch
Server = http://www2.futureware.at/~nickoe/msys2-mirror/msys/$arch/
```

+ �ü��±���`$directory\etc\pacman.d\mirrorlist.mingw32`, ��ustcԴ�ӵ���һ��:
``` python
## Primary
## msys2.org
Server = http://mirrors.ustc.edu.cn/msys2/mingw/i686/
Server = http://repo.msys2.org/mingw/i686
Server = https://downloads.sourceforge.net/project/msys2/REPOS/MINGW/i686
Server = http://www2.futureware.at/~nickoe/msys2-mirror/mingw/i686
```

+ �ü��±���`$directory\etc\pacman.d\mirrorlist.mingw64`, ��ustcԴ�ӵ���һ��:
``` python
## Primary
## msys2.org
Server = http://mirrors.ustc.edu.cn/msys2/mingw/x86_64
Server = http://repo.msys2.org/mingw/x86_64
Server = https://downloads.sourceforge.net/project/msys2/REPOS/MINGW/x86_64
Server = http://www2.futureware.at/~nickoe/msys2-mirror/mingw/x86_64
```

### ��pacman����ϵͳ�Լ���װ���
msys2��pacman�������, ��archlinux��һ���ġ�pacman��������:

``` bash
pacman -Syu       # ͬ������Ⲣ����ϵͳ������״̬ 
pacman -Ss vim    # ��������ֿ������ֺ���vim�������
pacman -S git     # ��װgit
pacman -R git     # ɾ��git
```

### ����Ҽ�����"msys here"
��windows 10Ϊ����
1 �ҵ�msys2�İ�װĿ¼`$directory`, �½�`msys2.bat`, ��������(��`$directory`�����Լ���·��):

``` bash
$directory\msys2_shell.cmd -mingw64 -where %cd%
```

2 `Win + r`����regedit, ����`HKEY_CLASSES_ROOT\Directory\Background\shell`, �½�**��**, ����Ϊ`msys2`(��cmd��Powershellͬһ�ȼ�)��
3 �Ҽ�msys2, ���½�**��**, ����Ϊ`command`��ѡ���½���`command`, �����ұߴ��ڵ�ֵΪ`$directory\msys2.bat`
4 �Ҽ�msys2, �½�**�ַ���**, ����Ϊicon, ֵΪ`$directory\msys2.ico`

�����������, `msys2`��ʹϵͳʶ�������Ҽ��˵���Ҫ�����Ϊ`msys2`��ѡ��, `command`�����ָ�������ĳ���λ��, `icon`�ַ���ָ��Ҫ�õ�ͼ���ַ��

�ο�����:

[�� MSYS2 ����пƴ��Դ](https://blog.csdn.net/liyuanbhu/article/details/56496501)

[pacman��������](https://www.2cto.com/kf/201704/620094.html)

[Ϊmsys2����Ҽ����ڵ�ǰĿ¼��](https://blog.csdn.net/u011924787/article/details/69485944)