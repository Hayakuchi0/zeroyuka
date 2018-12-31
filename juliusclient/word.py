import socket
import threading
from xml.etree import ElementTree
from abc import ABC, abstractmethod


class JuliusClientWord(ABC):

    def xmlToWord(self, receiveXmlString, encoding):
        rxsar = '<?xml version="1.0" encoding="' + encoding + '" ?><root>' + \
                receiveXmlString + '</root>'
        root = ElementTree.fromstring(rxsar)
        word = ''
        for whypo in root.iter('WHYPO'):
            word = word + whypo.attrib['WORD']
        if len(word) > 0:
            self.onGenerateWord(word=word)

    def start(self, address, encoding='utf-8'):
        func = self.__startthread
        thread = threading.Thread(target=func, args=[address, encoding])
        thread.start()

    def __startthread(self, address, encoding):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((address, 10500))
            receiveXml = ''
            self.connecting = True
            while self.connecting:
                data = sock.recv(65536)
                dataString = data.decode(encoding=encoding)
                dataString = dataString.replace(".\n", '')
                receiveXml = receiveXml + dataString
                if '</RECOGOUT>' in dataString:
                    self.xmlToWord(receiveXml, encoding)
                if '<INPUT STATUS="STARTREC" TIME="' in dataString:
                    receiveXml = ''

    def exit(self):
        self.connecting = False

    @abstractmethod
    def onGenerateWord(seld, word):
        pass
