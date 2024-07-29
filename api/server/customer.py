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
        "place": "|妖兽怪道|",
        "s_card": "仙符『凤凰卵』:随机获得三种鱼类食材",
        "f_card": "方符『奇门遁甲』:降低客人的入店频率",
        "money": "400~600円",
        "food": ["秘制小鱼干", "猪肉鳟鱼熏", "力量汤"],
    })
    Customer.Set_Customer("稗田阿求", {
        "name": "稗田阿求",
        "other_name": ["稗田阿求", "阿求", "aq", "阿Q", "阿q"],
        "like_food_tag": ["文化底蕴", "和风", "甜", "汤羹", "清淡", "高级", "流行·喜爱"],
        "unlike_food_tag": ["灼热", "重油", "咸", "流行·厌恶"],
        "like_drink_tag": ["清酒", "可加热"],
        "place": "|人间之里|",
        "s_card": "撰书『这也全都是妖怪干的吗』:获得一张签名色纸",
        "f_card": "口授『黑心店家的黑心历史』:清空店内气氛，降低正在用餐客人的心情值",
        "money": "500~800円",
        "food": ["豆腐味噌", "蔬菜专辑", "樱落雪"],
    })
    Customer.Set_Customer("上白泽慧音", {
        "name": "上白泽慧音",
        "other_name": ["上白泽慧音", "hy", "慧音", "老师"],
        "like_food_tag": ["文化底蕴", "和风", "中华", "家常", "清淡", "素", "流行·喜爱"],
        "unlike_food_tag": ["重油", "大份", "咸", "流行·厌恶"],
        "like_drink_tag": ["清酒", "烧酒", "利口酒"],
        "place": "|人间之里|",
        "s_card": ("国符『三种神器』:从以下四件神器中随机选择一种\n"
                   "  ○ 剑：随机奖励两种蔬菜\n"
                   "  ○ 镜：在一定时间内烹饪不消耗食材\n"
                   "  ○ 玉：随机解锁一个未完全解锁的稀客信息\n"
                   "  ○ 乡：吸引大量普客前来就餐"),
        "f_card": "国符『秘笈·头槌』:眩晕20s，期间无法移动。可以通过乱打方向键恢复",
        "money": "400~800円",
        "food": ["油豆腐", "诗礼银杏", "白雪"],
    })
    Customer.Set_Customer("茨木华扇", {
        "name": "茨木华扇",
        "other_name": ["茨木华扇", "华扇", "hs"],
        "like_food_tag": ["文化底蕴", "和风", "家常", "下酒"],
        "unlike_food_tag": ["实惠", "生", "辣"],
        "like_drink_tag": ["中酒精", "直饮", "古典"],
        "place": "|人间之里|",
        "s_card": "『猛兽的艺术用法』:召唤宠物老虎在店内演出，让排队和就座的客人每隔一段时间就会随机打赏1-30円",
        "f_card": "『断善修恶的禁欲考验』:客人只会点最便宜的食物和绿茶，持续30s",
        "money": "400~600円",
        "food": ["豆腐锅", "牛肉盖浇饭", "野味加农"],
    })


def customer_server_init():
    customer_query_init()
    customer_init()
