# ForFun
存放为了兴趣写的一些小东西的仓库

##  Get started

To start CoolQ, run the command below in `~/` as pwd.
```bash
sudo docker run -ti --rm --name cqhttp-test -v $(pwd)/coolq:/home/user/coolq -p 9000:9000 -p 5700:5700 -e COOLQ_ACCOUNT=1987739480 richardchien/cqhttp:latest
```

Start server
```bash
cd Project/ForFun/skhrBot/app
python3 bot.py
```

##  文件结构

### AFF: CPF的闲情逸致

用于下载AFF的FanFics

### skhrBot: 懒人的工具bot

一个用来做各种各样的功能集成的QQbot
目前的功能：
- 备忘

计划中的功能：
- 【日常】天气
- 游戏资料查询
