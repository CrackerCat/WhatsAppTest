import wx

APP_TITLE = "WhatsApp群控"

class MainWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,APP_TITLE,style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

        menuBar = wx.MenuBar()
        menu_App = wx.Menu()
        item_QuitApp = menu_App.Append(wx.ID_EXIT,"退出","退出应用")
        menuBar.Append(menu_App,"程序")
        self.Bind(wx.EVT_MENU,self.OnQuitApp,item_QuitApp)

        menu_About = wx.Menu()
        item_About = menu_About.Append(wx.ID_ABOUT,"关于程序","关于程序")
        menuBar.Append(menu_About,"关于")
        self.Bind(wx.EVT_MENU,self.OnAboutApp,item_About)
        self.SetMenuBar(menuBar)


        self.Center()
        pass

    def OnAboutApp(self,e):
        wx.MessageBox("本程序仅供企业内部使用,禁止用于非法用途","关于")

    def OnQuitApp(self,e):
        exit(0)


