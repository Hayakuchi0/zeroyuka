from abc import abstractmethod
from docomochat.talk import talk
from docomochat.userdata import getconfigpathuser, readuser
from juliusclient.word import JuliusClientWord


class JuliusClientDC(JuliusClientWord):

    def onGenerateWord(self, word):
        user = readuser(getconfigpathuser())
        self.onWordSend(word=word, user=user)
        message = talk(word, user)
        self.onMessageReceive(message=message, response={})

    @abstractmethod
    def onWordSend(self, word):
        pass

    @abstractmethod
    def onMessageReceive(self, message):
        pass
