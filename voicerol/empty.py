from voicerol.roltext import RolText


class RolEmpty(RolText):

    def installtool(self):
        pass

    def installed(self):
        return True

    def roltext(self, charanum, text):
        pass
