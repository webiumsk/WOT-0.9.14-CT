# 2016.02.14 12:42:34 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/messenger/formatters/users_messages.py
from gui import GUI_SETTINGS, makeHtmlString
from helpers import i18n
from messenger.m_constants import USER_ACTION_ID, MESSENGER_I18N_FILE
from messenger.proto.xmpp.xmpp_constants import CONTACT_LIMIT
_userTransferUserMsgKeys = {USER_ACTION_ID.FRIEND_ADDED: '#%s:client/information/addToFriends/message' % MESSENGER_I18N_FILE,
 USER_ACTION_ID.IGNORED_ADDED: '#%s:client/information/addToIgnored/message' % MESSENGER_I18N_FILE,
 USER_ACTION_ID.MUTE_SET: '#%s:client/information/setMuted/message' % MESSENGER_I18N_FILE,
 USER_ACTION_ID.MUTE_UNSET: '#%s:client/information/unsetMuted/message' % MESSENGER_I18N_FILE,
 USER_ACTION_ID.FRIEND_REMOVED: '#%s:client/information/removeFromFriends/message' % MESSENGER_I18N_FILE,
 USER_ACTION_ID.IGNORED_REMOVED: '#%s:client/information/removeFromIgnored/message' % MESSENGER_I18N_FILE}

def getUserActionReceivedMessage(actionIndex, user):
    if not GUI_SETTINGS.voiceChat and actionIndex in [USER_ACTION_ID.MUTE_SET, USER_ACTION_ID.MUTE_UNSET]:
        return
    else:
        if actionIndex in _userTransferUserMsgKeys:
            message = i18n.makeString(_userTransferUserMsgKeys[actionIndex], user.getName())
        else:
            message = None
        return message


def getBroadcastIsInCoolDownMessage(coolDown):
    return i18n.makeString('#%s:client/error/broadcastInCooldown' % MESSENGER_I18N_FILE, coolDown)


def makeFriendshipRequestText(user, error):
    result = []
    text = makeHtmlString('html_templates:lobby/friendshipRequest', 'title', ctx={'name': user.getFullName()})
    result.append(text)
    if error:
        text = makeHtmlString('html_templates:lobby/friendshipRequest/note', error.getErrorName(), ctx={'name': user.getFullName(),
         'rosterMaxCount': CONTACT_LIMIT.ROSTER_MAX_COUNT})
        result.append(text)
    return ''.join(result)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\formatters\users_messages.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:42:34 St�edn� Evropa (b�n� �as)
