import pyautogui as gui
import pyperclip as lip
import keyboard
import time

from const import const as cst
from tools import tools as tools
from api.server import query as server
from api.server import drink as server_drink
from api.server import customer as server_customer


def send_message(content):
    lip.copy(content)
    # 粘贴
    gui.hotkey("ctrl", "v")
    gui.write(["enter"])


def server_start():
    print("begin")

    while True:
        try_image("./image/qqHy_24.png")
        try_image("./image/qqQ_24.png")


def try_image(img_url):
    try:
        box = tuple[int, int, int, int](gui.locateOnScreen(img_url, confidence=0.9))
        gui.click(gui.center(box))
        time.sleep(0.2)
        content = try_lingXian()
        if tools.type_name(content, "str"):
            gui.click(gui.center(box))
            send_message("[ling_xian_bot]\n\n" + content)
        keyboard.press_and_release("esc")
    except Exception:
        return


def try_lingXian():
    try:
        box = list(gui.locateAllOnScreen("./image/ling_xian_24.png", confidence=0.9))
        for b in box:
            gui.click(gui.center(tuple[int, int, int, int](b)))
        return process_body(get_content())
    except Exception as e:
        return e


def get_content():
    gui.hotkey("ctrl", "c")
    import win32clipboard as w
    w.OpenClipboard()
    try:
        content = w.GetClipboardData()
    except Exception:
        content = ""
    w.CloseClipboard()
    return content


def process_body(content):
    print(content)
    str_list = tools.content_filter(content)
    body = server.Body
    for i in range(len(str_list)):
        if i == 0:
            if not server.Header.Analysis(str_list[0]):
                return False
        else:
            unknown = body.Analysis(str_list[i])
            if tools.type_name(unknown, "Query"):
                body = unknown
            if tools.type_name(unknown, "str"):
                return unknown
            if tools.type_name(unknown, "int"):
                if unknown == cst.ID_DRINK:
                    return process_drink(str_list[i + 1:])
                if unknown == cst.ID_CUSTOMER:
                    return process_customer(str_list[i + 1:])
    return body.Analysis("")


def process_customer(str_list):
    print(str_list)
    customer = server_customer.Customer
    query = server_customer.CustomerQuery
    if len(str_list) == 0:
        while not tools.type_name(query, "str"):
            query = query.Analysis("")
        return query
    for i in range(len(str_list)):
        if query.Analysis(str_list[i]):
            return customer.__other_name_str__()
        try:
            customer = server_customer.Customer.Search_Customer(str_list[0])
        except Exception as e:
            return e.__str__()
        query = query.Analysis("")
    return customer.__str__()


def process_drink(str_list):
    drink = server_drink.Drink
    for i in range(len(str_list)):
        drink = drink.Search_Drink(str_list[i])
    return drink.__str__()


if __name__ == '__main__':
    server.init()
    server_drink.drink_init()
    server_customer.customer_server_init()
    server_start()
