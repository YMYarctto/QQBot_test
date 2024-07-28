import datetime as date

QUERY = "QUERY"
BOT = "BOT"

log_file = "./utils/logs/chat.log"


def write(char, message):
    time = date.datetime.now()
    m = message.replace("\n", " $ ").replace("\r", "")
    s = (f'[{date.date.today()} '
         f'{time.hour.__str__().rjust(2,"0")}:'
         f'{time.minute.__str__().rjust(2,"0")}:'
         f'{time.second.__str__().rjust(2,"0")}]'
         f' {char}:{m}')
    print(s)
    with open(log_file, 'a') as f:
        f.write(s + '\n')
