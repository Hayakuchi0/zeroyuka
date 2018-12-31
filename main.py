from os import name
from os.path import exists
from juliustodocomo.cli import JuliusClientCLI
from docomochat.clitool import question
from docomochat.userdata import gettoolpath, getconfigpathuser, createuser
from voicerol.voiceroid import RolVoiceroid
from voicerol.empty import RolEmpty


class JCCLIToRolText(JuliusClientCLI):

    def setRolText(self, roltext):
        self.roltext = roltext

    def onWordSend(self, user, word):
        super().onWordSend(user, word)
        self.roltext.roltext(0, word)

    def onMessageReceive(self, response, message):
        super().onMessageReceive(response, message)
        self.roltext.roltext(1, message)


def installtools(roltext):
    if not roltext.installed():
        roltext.install()


def startcuimode():
    myconfigpath = getconfigpathuser()
    if not exists(myconfigpath):
        ans = question()
        createuser(myconfigpath, ans)
    roltext = RolEmpty(gettoolpath())
    if name == 'nt':
        roltext = RolVoiceroid(gettoolpath())
    roltext.install()
    print("マイク側のIPアドレスを入力してください。\n(4つのドット区切り10進数)")
    address = input()
    cliobj = JCCLIToRolText()
    cliobj.setRolText(roltext)
    cliobj.start(address=address)


startcuimode()
