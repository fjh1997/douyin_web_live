import time

from protobuf import message_pb2
from messages.base import Base

class ChatMessage(Base):
    def __init__(self):
        self.instance = message_pb2.ChatMessage()

    def __str__(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '【发言】' + self.user().nickname + ': ' + self.instance.content