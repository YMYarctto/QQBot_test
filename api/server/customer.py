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
    Customer.Set_Customer("露米娅", {
        "name": "露米娅",
        "other_name": ["露米娅", "lmy", "10", "⑩"],
        "like_food_tag": ["肉", "招牌", "生", "猎奇", "饱腹", "流行·喜爱"],
        "unlike_food_tag": ["昂贵", "下酒", "流行·厌恶"],
        "like_drink_tag": ["苦", "气泡"],
        "place": "|妖兽怪道|魔法森林|",
        "s_card": "月符『月光射线』:随机获得图鉴中收录的3种肉类",
        "f_card": "暗符『境界线』:黑暗笼罩你的料理区域，持续20s",
        "money": "150~350円",
        "food": ["臭豆腐", "炸八目鳗", "赛熊掌"],
    })
    Customer.Set_Customer("橙", {
        "name": "橙",
        "other_name": ["橙", "cheng"],
        "like_food_tag": ["肉", "水产", "甜", "烧烤", "重油", "流行·喜爱"],
        "unlike_food_tag": ["素", "猎奇", "灼热", "流行·厌恶"],
        "like_drink_tag": ["辛", "水果"],
        "place": "|妖兽怪道|魔法森林|",
        "s_card": "仙符『凤凰卵』:随机获得三种鱼类食材",
        "f_card": "方符『奇门遁甲』:降低客人的入店频率",
        "money": "400~600円",
        "food": ["秘制小鱼干", "猪肉鳟鱼熏", "力量汤"],
    })


def customer_server_init():
    customer_query_init()
    customer_init()
