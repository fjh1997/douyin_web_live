from protobuf import message_pb2

from messages.member import MemberMessage
from messages.like import LikeMessage
from messages.roomuserseq import RoomUserSeqMessage
from messages.gift import GiftMessage
from messages.social import SocialMessage
from messages.chat import ChatMessage

from colorama import init, Fore
# define colors
RED   = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
YELLOW = Fore.YELLOW
WHITE = Fore.WHITE
RESET = Fore.RESET
init()

def unpackMsgBin(filepath):
    response = message_pb2.Response()

    try:
        with open(filepath, 'rb') as f:
            response.ParseFromString(f.read())

            decodeMsg(response.messages)
    except Exception as e:
        pass

def decodeMsg(messages):
    for message in messages:
        try:
            if message.method == 'WebcastMemberMessage':
                member_message = MemberMessage()
                member_message.set_payload(message.payload)
                print(f"\n{RED}[+] {member_message} {RESET}")

            elif message.method == 'WebcastSocialMessage':
                social_message = SocialMessage()
                social_message.set_payload(message.payload)
                print(f"\n{GREEN}[+] {social_message} {RESET}")

            elif message.method == 'WebcastChatMessage':
                chat_message = ChatMessage()
                chat_message.set_payload(message.payload)
                print(f"\n{BLUE}[+] {chat_message} {RESET}")

            elif message.method == 'WebcastLikeMessage':
                like_message = LikeMessage()
                like_message.set_payload(message.payload)
                print(f"\n{CYAN}[+] {like_message} {RESET}")

            elif message.method == 'WebcastGiftMessage':
                gift_message = GiftMessage()
                gift_message.set_payload(message.payload)
                print(f"\n{MAGENTA}[+] {gift_message} {RESET}")

            elif message.method == 'WebcastRoomUserSeqMessage':
                room_user_seq_message = RoomUserSeqMessage() 
                room_user_seq_message.set_payload(message.payload)
                print(f"\n{YELLOW}[+] {room_user_seq_message} {RESET}")

        except Exception as e:
            print(e)