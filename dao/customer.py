from tools import tools as t
from dao.query import Query


# Customer: {
#     "__other_name": {
#         "NAME":"",
#         "like_food_tag": "",
#         "unlike_food_tag": "",
#         "like_drink_tag": "",
#         "PLACE": "",
#         "S_CARD": "",
#         "F_CARD": "",
#         "MONEY": "",
#         "food": "",
#     },
#     "__customer": {
#         "a": "a"
#     }
# }


class CustomerList:
    class Customer:
        def __init__(self, v):
            self.NAME = v["name"]
            self.other_name = v["other_name"]
            self.like_food_tag = v["like_food_tag"]
            self.unlike_food_tag = v["unlike_food_tag"]
            self.like_drink_tag = v["like_drink_tag"]
            self.PLACE = v["place"]
            self.S_CARD = v["s_card"]
            self.F_CARD = v["f_card"]
            self.MONEY = v["money"]
            self.food = v["food"]

        def __str__(self):
            s_like_food = "|"
            for v in self.like_food_tag:
                s_like_food += f'{v}|'
            s_unlike_food = "|"
            for v in self.unlike_food_tag:
                s_unlike_food += f'{v}|'
            s_like_drink = "|"
            for v in self.like_drink_tag:
                s_like_drink += f'{v}|'
            return (f'{self.NAME}\n\n'
                    f'☆偏好：\n'
                    f' ·菜肴喜好：{s_like_food}\n'
                    f' ·菜肴厌恶：{s_unlike_food}\n'
                    f' ·酒水喜好：{s_like_drink}\n'
                    f'☆持有：{self.MONEY}\n'
                    f'☆出现地区：{self.PLACE}\n'
                    f'☆菜谱：\n'
                    f' ·Lv1 -> {self.food[0]}\n'
                    f' ·Lv2 -> {self.food[1]}\n'
                    f' ·Lv3 -> {self.food[2]}\n'
                    f'☆符卡：\n'
                    f' ·奖励符卡：{self.S_CARD}\n'
                    f' ·惩罚符卡：{self.F_CARD}')

        def __other_name_str__(self):
            s = "查询到以下别名：\n| "
            for name in self.other_name:
                s += f'{name} | '
            return s

    def __init__(self):
        self.__customer = dict()
        self.__other_name = dict()

    def Set_other_name(self, s):
        for name in self.__customer[s].other_name:
            self.o_name(name, s)

    def o_name(self, other_name, s):
        self.__other_name[other_name] = s

    def Set_Customer(self, name, v):
        self.__customer[name] = self.Customer(v)
        self.Set_other_name(name)

    def Search_Customer(self, name):
        if name in self.__other_name.keys():
            return self.__customer[self.__other_name[name]]
        if name in self.__customer.keys():
            return self.__customer[name]
        return Exception("未找到角色，发送“角色 别名列表”以查看所有别名")

    def __other_name_str__(self):
        s = "别名列表：\n"
        for name in self.__customer:
            s += f'{name}：| '
            for o_name in self.__customer[name].other_name:
                s += f'{o_name} | '
            s += "\n"
        return s


class CustomerQuery(Query):
    def Analysis(self, query: str) -> any:
        if not self.Contain(query):
            return False
        elif not t.type_name(self.dict[query], "str"):
            return self.dict[query]
        return self.dict[""]


def CustomerQueryInit(content):
    return CustomerQuery(content=content)


def CustomerListInit():
    return CustomerList()
