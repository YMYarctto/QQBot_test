import pyautogui as gui
import pyperclip as lip
import keyboard
import time

from tools import content as cont
from api.server import init as server


def send_message(content):
    lip.copy(content)
    # 粘贴
    gui.hotkey("ctrl", "v")
    gui.write(["enter"])


def server_start():
    print("begin")

    while True:
        try:
            box = tuple[int, int, int, int](gui.locateOnScreen("./image/qqHy_24.png", confidence=0.8))
            gui.click(gui.center(box))
            content = try_lingXian()
            if type(content).__name__ == "str":
                time.sleep(0.5)
                gui.click(gui.center(box))
                send_message("[ling_xian_bot]\n\n"+content)
            keyboard.press_and_release("esc")
        except gui.ImageNotFoundException:
            continue


def try_lingXian():
    try:
        box = tuple[int, int, int, int](gui.locateOnScreen("./image/ling_xian_24.png", confidence=0.8))
        gui.click(gui.center(box))
        return process_content(get_content())
    except gui.ImageNotFoundException as e:
        return e


def get_content():
    gui.hotkey("ctrl", "c")
    import win32clipboard as w
    w.OpenClipboard()
    content = w.GetClipboardData()
    w.CloseClipboard()
    return content


def process_content(content):
    print(content)
    str_list = cont.content_filter(content)
    if len(str_list) == 0:
        return False
    if len(str_list) >= 1:
        if not server.Analysis_Header(str_list[0], ""):
            return False
    if len(str_list) == 2:
        return server.Analysis_Body(str_list[1], "")
    if len(str_list) >= 3:
        return server.Analysis_Body(str_list[1], str_list[2])
    return server.Analysis_Body("", "")


if __name__ == '__main__':
    server.init()
    server_start()
