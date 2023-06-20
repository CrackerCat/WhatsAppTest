import wx
import ConfigManager
import uiautomator2
import uiautomator2 as u2
import WhatsApp
from enum import Enum

APP_TITLE = "WhatsApp群控"

class MainWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,APP_TITLE,style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        self.SetSize(800,600)


        menuBar = wx.MenuBar()
        menu_App = wx.Menu()
        item_QuitApp = menu_App.Append(-1,"退出","退出应用")
        menuBar.Append(menu_App,"程序")
        self.Bind(wx.EVT_MENU,self.OnQuitApp,item_QuitApp)

        menu_About = wx.Menu()
        item_About = menu_About.Append(-1,"关于程序","关于程序")
        menuBar.Append(menu_About,"关于")
        self.Bind(wx.EVT_MENU,self.OnAboutApp,item_About)
        self.SetMenuBar(menuBar)

        #建立主面板
        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)

        #创建养号选项卡
        tab_养号功能 = wx.Panel(notebook)
        tabSizer_养号 = wx.GridBagSizer(5,5)
        tab_养号功能.SetSizer(tabSizer_养号)

        #创建沟通账号文件相关控件
        text_设置沟通账号 = wx.StaticText(tab_养号功能, label="沟通账号文件:")
        self.ChatUserSrc = wx.TextCtrl(tab_养号功能,size=(400,25))
        self.ChatUserSrc.SetLabelText(ConfigManager.Instance.ReadConfig("ContactUserFile"))
        btn_设置沟通账号 = wx.Button(tab_养号功能,label="设置")
        tabSizer_养号.Add(text_设置沟通账号, pos=(2, 4),flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        tabSizer_养号.Add(self.ChatUserSrc, pos=(2, 6), flag=wx.ALIGN_RIGHT)
        tabSizer_养号.Add(btn_设置沟通账号, pos=(2, 7), flag=wx.EXPAND)
        self.Bind(wx.EVT_BUTTON,self.OnSetUserContactList,btn_设置沟通账号)

        #设置沟通内容文件相关控件
        text_设置沟通内容 = wx.StaticText(tab_养号功能, label="沟通内容文件:")
        self.ChatContentSrc = wx.TextCtrl(tab_养号功能,size=(400,25))
        self.ChatContentSrc.SetLabelText(ConfigManager.Instance.ReadConfig("ContentFile"))
        btn_设置沟通内容  = wx.Button(tab_养号功能,label="设置")
        tabSizer_养号.Add(text_设置沟通内容, pos=(4, 4),flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        tabSizer_养号.Add(self.ChatContentSrc, pos=(4, 6), flag=wx.ALIGN_RIGHT)
        tabSizer_养号.Add(btn_设置沟通内容, pos=(4, 7), flag=wx.EXPAND)
        self.Bind(wx.EVT_BUTTON,self.OnSetContactContent,btn_设置沟通内容)

        #设置发送消息间隔
        text_设置聊天间隔 = wx.StaticText(tab_养号功能, label="聊天间隔(秒):")
        self.ChatTimePeriod = wx.TextCtrl(tab_养号功能,size=(40,25))
        tabSizer_养号.Add(text_设置聊天间隔, pos=(6, 4),flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        tabSizer_养号.Add(self.ChatTimePeriod, pos=(6, 6), flag=wx.ALIGN_LEFT)

        #开始养号
        btn_开始养号 = wx.Button(tab_养号功能,label="开始养号",size=(100,100))
        tabSizer_养号.Add(btn_开始养号, pos=(10, 6), flag=wx.Center)
        self.Bind(wx.EVT_BUTTON,self.OnStartYangHao,btn_开始养号)

        notebook.AddPage(tab_养号功能, "养号功能")

        # # 创建选项卡2
        # tab2 = wx.Panel(notebook)
        # text_ctrl2 = wx.TextCtrl(tab2, style=wx.TE_MULTILINE)
        #
        # sizer2 = wx.BoxSizer(wx.VERTICAL)
        # sizer2.Add(text_ctrl2, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        # tab2.SetSizer(sizer2)
        #
        # notebook.AddPage(tab2, "选项卡2")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        panel.SetSizer(sizer)


        self.Center()
        pass

    def OnStartYangHao(self,e):
        d = u2.connect()  # connect to device
        d.settings['wait_timeout'] = 5  # 控件查找默认等待时间(默认20s)
        WhatsApp.StartApp(d)
        WhatsApp.SendMessage(d)
        pass

    def OnSetContactContent(self,e):
        wildcard = "Text files (*.txt)|*.txt"
        dialog = wx.FileDialog(self, message="选择要沟通的内容txt文件", wildcard=wildcard, style=wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
            ConfigManager.Instance.WriteConfig("ContentFile",path)
            self.ChatContentSrc.SetLabelText(path)
    def OnSetUserContactList(self,e):
        wildcard = "Text files (*.txt)|*.txt"
        dialog = wx.FileDialog(self, message="选择要沟通的账号txt文件", wildcard=wildcard, style=wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
            ConfigManager.Instance.WriteConfig("ContactUserFile",path)
            self.ChatUserSrc.SetLabelText(path)

    def OnAboutApp(self,e):
        wx.MessageBox("本程序仅供企业内部使用,禁止用于非法用途","关于")

    def OnQuitApp(self,e):
        exit(0)


