import datetime as date

chat_file = "./utils/logs/chat.log"
error_file = "./utils/logs/error.log"


def get_time() -> str:
    time = date.datetime.now()
    return (f'{date.date.today()} '
            f'{time.hour.__str__().rjust(2, "0")}:'
            f'{time.minute.__str__().rjust(2, "0")}:'
            f'{time.second.__str__().rjust(2, "0")}]')


def write(char: str, message: str) -> None:
    time = get_time()
    m = message.replace("\n", " $ ").replace("\r", "")
    s = f'[{time} {char}:{m}'
    print(s)
    with open(chat_file, 'a') as f:
        f.write(s + '\n')


def error(e: Exception) -> None:
    time = get_time()
    s = f'{time} [Error]:{e.__str__()}'
    print(s)
    print(e.__traceback__.tb_frame.f_globals["__file__"])
    print(e.__traceback__.tb_lineno)
    with open(error_file, 'a') as f:
        f.write(s + '\n')
