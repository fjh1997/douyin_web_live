﻿
抖音web直播间([live.douyin.com](https://live.douyin.com))弹幕抓取
--

**屏幕效果截图**

![enter image description here](https://github.com/gll19920817/tiktok_live/blob/main/WX20211129-144919@2x.png?raw=true)

**项目思路**

1. Selenium 无窗口且detach模式打开live直播间
2. mitmproxy 捕获live.douyin.com http请求并保存响应为指定目录下文件
3. watchdog监控步骤2指定目录下文件变化后反序列化文件(application/protobuf格式)
4. 反序列化弹幕消息分类后terminal输出且入库(mongodb)

**使用方法**

5. 安装[python3](https://www.python.org/downloads/)
6. clone本项目，terminal进入项目目录，执行 `pip install requirements.txt`
7. 安装[mitmproxy](https://mitmproxy.org/) terminal执行`mitmproxy -s scripts/mitiproxy.py` (scripts/mitiproxy.py见项目)
8. terminal执行 `python3 main.py`

**注意事项**

1. 本源代码仅可作学习目的修改！
2.  emm... 🤔