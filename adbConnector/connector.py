import os

class Connector:
    def __init__(self):
        self.devices = ''

    def exec(self,shell:str):
        output = os.popen(shell)
        print(output.read())
        return output.read()

    def connect(self):
        self.exec('adb usb')
        self.devices = self.exec('adb devices')

    def screenCap(self, filepath):
        self.exec('adb exec-out screencap -p > ' + filepath)

    def tap(self,x,y):
        self.exec(f'adb shell input tap {x} {y}')