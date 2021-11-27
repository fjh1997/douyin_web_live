import time

from protobuf import message_pb2
from messages.base import Base

class GiftMessage(Base):
    def __init__(self):
        self.instance = message_pb2.GiftMessage()

    def __str__(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '【送礼】' + self.instance.common.describe