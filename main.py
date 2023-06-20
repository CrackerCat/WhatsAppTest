import random
import time
import wx
import MainWindow


# 生成随机长度的字母
def generateRandomText(length):
    letters = "abcdefghijklmnopqrstuvwxyz "
    random_letters = ''.join(random.choice(letters) for _ in range(length))
    return random_letters

if __name__ == '__main__':
    app = wx.App()
    app.SetAppName("WhatsApp群控")
    app.Frame = MainWindow.MainWindow()
    app.Frame.Show()
    app.MainLoop()
    exit(0)



