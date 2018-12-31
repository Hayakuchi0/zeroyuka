from .jcdc import JuliusClientDC


class JuliusClientCLI(JuliusClientDC):

    def onWordSend(self, user, word):
        print("[" + user["option"]["nickname"] + "]" + word)

    def onMessageReceive(self, response, message):
        print("[ゼロ]:" + message)

    def start(self, address, encoding='utf-8'):
        super().start(address, encoding)
        print("####talk start!####")
        print("If you end talk, enter the 'q' and Return.")
        text = ""
        while text is not "q":
            text = input()
            print("####talk end####")
            self.exit()
