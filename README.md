## 抖音直播间(web)弹幕抓取

***Screenshot***

![enter image description here](https://github.com/gll19920817/tiktok_live/blob/main/WX20211129-144919@2x.png?raw=true)

***Pre Requirements***

``Python3 & Charles``

***Installation***

 1. `git clone https://github.com/gll19920817/douyin_web_live`
 2. `pip install -r requirements.txt`
 3. `Open Charles > Tools > Mirror > Mirrors Setting`
	 - `Enable Mirror`
	 - `Save to a folder, eg:/Users/username/charles/autosave`
	 - `Add location: https://live.douyin.com/webcast/im/fetch/`
4. `Change /main.py Watcher Class directory parameter to folder that Step 3 choose, eg: /Users/username/charles/autosave`
5. `python3 main.py`

***Final thoughts***
 1. Persists data to db, eg: mongo ✅
 2. Charles alternative: maybe mitmproxy & scapy
 
