from dao import customer

Customer = customer.CustomerListInit()
CustomerQuery = customer.CustomerQueryInit("")


def customer_query_init():
    CustomerQuery.Set("别名列表", True)
    inner = CustomerQuery.Group("", "发送“角色 {角色名/角色别名}”以查看角色信息")
    inner.Set("别名", True)


def customer_init():
    Customer.Set_Customer("莉格露", {
        "name": "莉格露",
        "other_name": ["莉格露", "lgl", "虫子", "萤火虫"],
        "like_food_tag": ["肉", "甜", "生", "猎奇"],
        "unlike_food_tag": ["素", "清淡", "凉爽"],
        "like_drink_tag": ["低酒精", "可加冰"],
        "place": "|妖兽怪道|魔法森林|",
        "s_card": "灯符『荧光现象』:顾客出现速度+30%，持续30秒",
        "f_card": "蠢符『夜虫龙卷』:赶走所有客人且不结账",
        "money": "200~400円",
        "food": ["露水煮蛋", "香炸蝉蜕", "幻昙华糕"],
    })


def customer_server_init():
    customer_query_init()
    customer_init()
