### 喜马拉雅音频下载器

本下载器根据专辑ID来下载音频，例如：

`https://www.ximalaya.com/xiangsheng/9739820/`中的`9739820`

详细的命令行参数如下：
```
C:\GitHub\Spider\Ximalaya>python ximalaya.py -h
usage: ximalaya.py [-h] -i XID [-p PATH]

optional arguments:
  -h, --help            show this help message and exit
  -i XID, --xid XID     专辑ID
  -p PATH, --path PATH  下载路径，默认下载到桌面
```