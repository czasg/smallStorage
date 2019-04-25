git chown -R root:root czaOrz  # 后面是目录，更改这个目录的权限


创建自己的服务器：
1、在服务器端：
首先 mkdir /gits/cza.git  创建路径
然后 git init --bare /gits/cza.git  初始化
再   chown -R cza:cza /gits/cza.git 授权

然后就可以远程拉分支了，但是还要在要在服务器端的/etc/.ssh打开三个开关
RSAAuthentication yes
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys

本地端拉代码，并注册ssh
ssh czaOrz@47.101.42.79 'cat >> .ssh/authorized_keys' < ~/.ssh/id_rsa.pub
git clone czaOrz@47.101.42.79:/gits/czaOrz.git


