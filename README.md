**抖音直播间(web)弹幕抓取**

Pre Requirements
- Python3
- Charles

 1. `git clone https://github.com/gll19920817/tiktok_live`
 2. `pip install -r requirements.txt`
 3. `Open Charles > Tools > Mirror > Mirrors Setting`
	 - `Enable Mirror`
	 - `Save to a folder, eg:/Users/douyin/feeds/`
	 - `Add location: https://live.douyin.com/webcast/im/fetch/`
4. `change main.py Watcher directory parameter to folder that Step 3 	  choose, eg: /Users/douyin/feeds/`
5. `python3 main.py`

Final thoughts :
 1. Save data to mongodb
 2. Charles alternative: maybe mitmproxy & scapy
