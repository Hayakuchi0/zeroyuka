from abc import ABC, abstractmethod


class RolText(ABC):

    def __init__(self, toolpath):
        self.toolpath = toolpath
        self.install()

    @abstractmethod
    def installtool(self):
        pass

    @abstractmethod
    def installed(self):
        pass

    @abstractmethod
    def roltext(self, charanum, text):
        pass

    def install(self):
        if not self.installed():
            self.installtool()
