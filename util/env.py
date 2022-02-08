import os
import platform

class EnvManager:
    def __init__(self):
        self.envdict = os.environ
        self.system = platform.system()

    def checkAdbEnv(self):
        if self.envdict.get("PATH").count("adb") > 0:
            dirs = self.envdict.get("PATH").split(";")
            for dir in dirs:
                if dir.count("adb") > 0:
                    return (os.path.exists(dir) and os.path.exists(dir + "\\adb.exe")) or (os.path.exists(dir) and os.path.exists(dir + "\\adb"))
        return False

    def setAdbEnv(self):
        if self.system == "Windows":
            self.envdict["PATH"] = os.path.abspath("..")+"\\"+"adb" + ";" + self.envdict["PATH"]
        if self.system == "Linux":
            self.envdict["PATH"] = os.path.abspath("..")+"\\"+"adb" + ":" + self.envdict["PATH"]
