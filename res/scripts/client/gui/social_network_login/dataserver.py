# 2016.02.13 15:04:47 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/social_network_login/DataServer.py
import base64
import os
import hashlib
from RequestHandler import RequestHandler
from Crypto.Cipher import AES
from Crypto.Util import Counter
import BigWorld
from debug_utils import LOG_DEBUG
from standalone.social_network_login import Server

class DataServer(Server):

    def __init__(self, name, dataReceivedHandler, encryptToken):
        Server.__init__(self, name, RequestHandler)
        self.__encryptToken = encryptToken
        if self.__encryptToken:
            self.__tokenSecret = hashlib.sha1(os.urandom(128)).hexdigest()[:16]
        self.__dataReceivedHandler = dataReceivedHandler

    def keepData(self, token, spaID):
        BigWorld.callback(0, lambda : self.__dataReceivedHandler(token, spaID, self._decryptToken))

    @property
    def tokenSecret(self):
        if self.__encryptToken:
            return self.__tokenSecret

    def _logStatus(self):
        LOG_DEBUG(self._currentStatus)

    def _decryptToken(self, token):
        if self.__encryptToken:
            cipher = AES.new(self.__tokenSecret, AES.MODE_CTR, counter=Counter.new(128))
            return cipher.decrypt(base64.urlsafe_b64decode(token))
        else:
            return token
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\social_network_login\dataserver.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:04:47 St�edn� Evropa (b�n� �as)
