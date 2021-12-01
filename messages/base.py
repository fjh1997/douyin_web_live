from datetime import datetime
from store.mongo import MongoStore

from config.helper import config

class Base:

    instance = None

    def set_payload(self, payload):
        self.instance.ParseFromString(payload)

    def extra_info(self):
        return dict()
        
    def user(self):
        return self.instance.user

    def persists(self):
        if config()['mongo']['enabled'] != 'on':
            return

        try:
            store = MongoStore()
            store.set_collection('user')

            user = self.user()

            store.replace_one({
                "id": user.id
            }, {
                "id": user.id,
                "shortId": user.shortId,
                "nickname": user.nickname,
                "gender": user.gender,
                "avatar_thumb": user.avatarThumb.urlList[0],
                "followInfo": {
                    "followingCount": user.followInfo.followingCount,
                    "followerCount": user.followInfo.followerCount
                }
            }, upsert=True)

            store.set_collection(self.instance.common.method)

            msg = {
                "msgId": self.instance.common.msgId,
                "roomId": self.instance.common.roomId,
                "userId": user.id,
                'content': self.format_content(),
                'created_at': datetime.today().replace(microsecond=0)
            }

            if len(self.extra_info()):
                msg.update(self.extra_info())

            store.insert_one(msg)
        except Exception as e:
            print(self.instance.common.method + ' persists error')


    def __str__(self):
        pass

