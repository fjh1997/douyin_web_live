import time

from protobuf import message_pb2
from messages.base import Base

class MemberMessage(Base):
    def __init__(self):
        self.instance = message_pb2.MemberMessage()

    def __str__(self):
        template = self.instance.common.displayText.defaultPattern
        nickname = self.user().nickname

        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '【进入直播间】' + template.replace('{0:user}', nickname).replace('{1:string}', '')