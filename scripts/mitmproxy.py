# ! IMPORT ! make sure you ran mitmproxy with this script, 
# eg: `/path/to/mitmproxy -s mitmproxy.py`

import uuid
from mitmproxy import http

class Writer:
    def response(self, flow: http.HTTPFlow) -> None:
        if flow.request.host == 'live.douyin.com':
            with open('/Users/geng/douyin_live/' + uuid.uuid4().hex, 'wb') as f:
                f.write(bytes(flow.response.content))

addons = [Writer()]
