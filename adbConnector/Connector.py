import os
import time


class Connector:
    def __init__(self):
        pass

    @classmethod
    def connect(cls):
        while not cls.checkConnect():
            print("connect.....")
            os.popen("adb usb")
            time.sleep(2)
        print("connect success")

    @classmethod
    def checkConnect(cls):
        return os.popen("adb devices").read().count("device")>1

    # click
    @classmethod
    def tap(cls,x,y):
        if not cls.checkConnect():
            print("connection fail")
            return
        os.popen(f"adb shell input tap {x} {y}")

    # screen capture
    def screencap(self):
        os.popen("adb exec-out screencap -p > ../cache.png")
        print("screen image has been saved in cache.png")
