from store.mongo import MongoStore

class Base:

    instance = None

    def set_payload(self, payload):
        self.instance.ParseFromString(payload)
        
    def user(self):
        return self.instance.user

    def persists(self):
        try:
            store = MongoStore()
            store.set_collection('user')

            user = self.user()

            store.insert_one({
                "id": user.id,
                "shortId": user.shortId,
                "nickname": user.nickname,
                "gender": user.gender,
                "avatar_thumb": user.avatarThumb.urlList[0],
                "followInfo": {
                    "followingCount": user.followInfo.followingCount,
                    "followerCount": user.followInfo.followerCount
                }
            })

            store.set_collection(self.instance.common.method)
            store.insert_one({
                "msgId": self.instance.common.msgId,
                "roomId": self.instance.common.roomId,
                "userId": user.id,
                'content': self.format_content()
            })
        except Exception as e:
            print(self.instance.common.method + 'persists error')


    def __str__(self):
        pass

