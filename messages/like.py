import time

from protobuf import message_pb2
from messages.base import Base

class LikeMessage(Base):
    def __init__(self):
        self.instance = message_pb2.LikeMessage()

    def format_content(self):
        return self.user().nickname + ' 点赞了直播间（' + str(self.instance.count) + '连赞）'

    def __str__(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '【点赞】' +  self.format_content()
