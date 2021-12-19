fork from https://github.com/coffeehat/BIT-srun-login-script

# 概述
北京航空航天大学校园网自动登陆脚本
详情见 https://zhuanlan.zhihu.com/p/122556315

## 用户密码配置

在`always_online.py`中配置自己的用户名和密码

## 开机自启动

如果有开机自启动需求, 往下看

### Ubuntu 20.04

编辑目录`systemd`下的`buaalogin.service`文件, 并将`ExecStart`属性中的python路径及程序路径正确设置

复制`buaalogin.service`文件至`/lib/systemd/system/`文件夹中。

参考运行以下命令：
```bash
sudo systemctl daemon-reload # 加载文件
sudo systemctl start buaalogin.service # 启动服务

sudo systemctl enable buaalogin.service # 开机自启动
sudo systemctl disable buaalogin.service # 取消开机自启动
```

在文件`/var/log/buaalogin.log`中查看运行日志
