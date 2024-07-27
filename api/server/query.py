from dao import query
from const import const

Header = query.QueryInit(False)
Body = query.QueryInit("未识别字段\n发送<帮助>以获取列表")


def init():
    header_init()
    body_init()


def header_init():
    Header.Set("铃仙", query.QueryInit(True))


def body_init():
    Body.Set("帮助", query.QueryInit("{帮助}"))
    Body.Set("关于", query.QueryInit("这里是ling_xian_bot，一款东方夜雀食堂信息查询bot，发送[帮助]可查看使用说明\n项目地址：\n"
                                     "https://github.com/YMYarctto/QQBot_test"))
    drink = Body.Group("酒水", "输入酒水tag以查询")
    drink.Set_All(["无酒精", "低酒精", "中酒精", "高酒精", "可加冰", "可加热", "烧酒", "利口酒", "清酒",
                   "西洋酒", "啤酒", "鸡尾酒", "直饮", "水果", "甘", "辛", "苦", "气泡", "古典", "提神", "现代"],
                  const.ID_DRINK)
