import requests
from os import sep, makedirs
from os.path import exists, isdir
from subprocess import Popen
from zipfile import ZipFile
from time import sleep
from xml.etree import ElementTree
from voicerol.roltext import RolText

TTU = 'https://www.dropbox.com/s/7q29bqqkqxhoosl/tamiyasu_talk_1_15_0.zip?dl=1'


class RolVoiceroid(RolText):

    def __init__(self, toolpath):
        super().__init__(toolpath)
        self.readxml()

    def getvoiceroidpath(self):
        return self.toolpath + sep + "voiceroid"

    def gettamiyasuzippath(self):
        return self.getvoiceroidpath() + sep + "tamiyasu_talk.zip"

    def gettamiyasupath(self):
        return self.getvoiceroidpath() + sep + "tamiyasu_talk"

    def gettamiyasuexepath(self):
        return self.gettamiyasupath() + sep + "vrx.exe"

    def gettamiyasuxmlpath(self):
        return self.gettamiyasupath() + sep + "vrx.xml"

    def performtamiyasu(self, option):
        cmd = self.gettamiyasuexepath() + option
        Popen(cmd)

    def downloadtamiyasu(self):
        savezippath = self.gettamiyasuzippath()
        if not exists(savezippath):
            url = TTU
            downloads_data = requests.get(url)
            savepath = savezippath
            with open(savepath, 'wb') as saveFile:
                saveFile.write(downloads_data.content)
        return exists(savezippath)

    def installtool(self):
        if not isdir(self.getvoiceroidpath()):
            makedirs(self.getvoiceroidpath())
        extractpath = self.gettamiyasupath()
        if not exists(extractpath):
            downloadcomplete = False
            while not downloadcomplete:
                downloadcomplete = self.downloadtamiyasu()
            with ZipFile(self.gettamiyasuzippath()) as tamiyasuzip:
                tamiyasuzip.extractall(self.getvoiceroidpath())
        if not self.installed():
            self.performtamiyasu("")
            while not self.installed():
                sleep(1)
        self.readxml()
        return exists(self.gettamiyasuexepath())

    def readxml(self):
        if self.installed():
            tree = ElementTree.parse(self.gettamiyasuxmlpath())
            root = tree.getroot()
            self.chara = {}
            i = 0
            for swt in root.iter("sWindowTitle"):
                name = swt.text
                self.chara[i] = name.replace("VOICEROID2 ", "")
                i += 1

    def installed(self):
        return exists(self.gettamiyasuxmlpath())

    def roltext(self, charanum, text):
        self.performtamiyasu(" \"" + self.chara[charanum] + ">"+text+"\"")
