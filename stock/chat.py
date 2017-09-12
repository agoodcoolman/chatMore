
import itchat
from itchat.content import *
from worker import *
from resolveMessage import *
@itchat.msg_register(TEXT, isGroupChat=True, isFriendChat=True)
def text_reply(msg):
    if msg.isAt:
        message = resolveMessage(msg)
        msg.user.send(u'@%s\u2005  %s' % (
            msg.actualNickName, message))




@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    msg.user.send('%s: %s' % (msg.type, msg.text))

def send_message(chatroomName, userName, stockName):
    chatrooms = itchat.get_chatrooms
    for chatroom in chatrooms:
        pass
        # itchat.send(stockName, toUserName=chatroom[userName])


if __name__ == '__main__':
    start_proc()
    itchat.auto_login(False)
    itchat.run(True)