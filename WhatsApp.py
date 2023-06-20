import time
import uiautomator2
import uiautomator2 as u2
from enum import Enum

#标记当前界面的状态
class AppState(Enum):
    Unknown = 0
    #主页
    Home = 1
    #选择联系人
    ContactPick = 2
    #聊天对话
    Conversation = 3

def StartApp(d:uiautomator2.Device):
    d.app_start("com.whatsapp")

def CheckStatus(d:uiautomator2.Device):
    对话按钮 = d.xpath("//*[@content-desc='对话']/android.widget.FrameLayout[1]/android.widget.ImageView[1]")
    if 对话按钮.exists:
        return AppState.Home
    聊天框 = d(resourceId="com.whatsapp:id/conversation_contact")
    if 聊天框.exists:
        return AppState.Conversation
    选择联系人 = d(resourceId="com.whatsapp:id/contact_list")
    if 选择联系人.exists:
        return AppState.ContactPick
    return AppState.Unknown

def LocateToHome(d:uiautomator2.Device):
    status = CheckStatus(d)
    if status == AppState.ContactPick:
        search_back = d(resourceId="com.whatsapp:id/search_back")
        if search_back.exists:
            search_back.click()
        time.sleep(1)
        back_button = d.xpath("//*[@content-desc='转到上一层级']")
        if back_button.exists:
            back_button.click()
        return
    if status == AppState.Conversation:
        back_button = d(resourceId="com.whatsapp:id/whatsapp_toolbar_home")
        if back_button.exists:
            back_button.click()
        return
    return

def SendMessage(d:uiautomator2.Device):
    LocateToHome(d)
    time.sleep(1)
    发送消息按钮 = d(resourceId="com.whatsapp:id/fabText")
    if not 发送消息按钮.exists:
        print("没找到发送消息按钮")
        return
    发送消息按钮.click()
    time.sleep(1)

    搜索按钮 = d(resourceId="com.whatsapp:id/menuitem_search")
    if not 搜索按钮.exists:
        print("没找到搜索按钮")
        return
    搜索按钮.click()
    time.sleep(1)

    搜索框 = d(resourceId="com.whatsapp:id/search_src_text")
    if not 搜索框.exists:
        print("没找到搜索框")
        return
    搜索框.set_text("133")
    time.sleep(1)

    用户名控件 = d(resourceId="com.whatsapp:id/contactpicker_row_name")
    对话按钮 = d(resourceId="com.whatsapp:id/buttons")
    if 对话按钮.exists:
        对话按钮.click()
    elif 用户名控件.exists:
        用户名 = 用户名控件.get_text()
        if 用户名.find("没有找到“") == 0:
            print("没找到联系人")
            return
        用户名控件.click()
    time.sleep(1)

    发送消息框 = d(resourceId="com.whatsapp:id/entry")
    if not 发送消息框.exists:
        print("没找到发送消息框")
        return