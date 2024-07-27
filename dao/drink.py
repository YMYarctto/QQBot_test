class DrinkList:
    class Drink:
        def __init__(self, name, tag, price):
            self.NAME = name
            self.tag = tag
            self.PRICE = price

        def __str__(self):
            rj = self.PRICE
            lj = self.NAME
            if self.NAME == "果味SOUR" or self.NAME == "超ZUN啤酒":
                lj += "—"
            if len(self.PRICE) == 1:
                rj = f'—{self.PRICE}'
            return f'{lj.ljust(6, "—")}——{rj}円'

        def tag_Contain(self, v):
            return v in self.tag

    def __init__(self):
        self.__drink = []

    def Set_Drink(self, name, tag, price):
        self.__drink.append(self.Drink(name=name, tag=tag, price=price))

    def Search_Drink(self, tag):
        drink_list = DrinkListInit()
        for drink in self.__drink:
            print(drink.__str__())
            if drink.tag_Contain(tag):
                drink_list.Set_Drink(drink.NAME, drink.tag, drink.PRICE)
        return drink_list

    def __str__(self):
        s = "查找到以下酒水：\n"
        if len(self.__drink) == 0:
            return f"未找到符合tag的酒水"
        for v in self.__drink:
            s += v.__str__() + "\n"
        return s


def DrinkListInit():
    return DrinkList()
