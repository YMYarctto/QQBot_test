from dao.query import query

Header = query.QueryInit(False)
Body = query.QueryInit("未识别字段\n发送<帮助>以获取列表")


def init():
    header_init()
    body_init()


def header_init():
    Header.Set("铃仙", query.QueryInit(True))


def body_init():
    Body.Set("帮助", query.QueryInit("test message"))


def Analysis_Header(q, c):
    print(Header.Self())
    return Header.Analysis(q, c)


def Analysis_Body(q, c):
    print(Body.Self())
    return Body.Analysis(q, c)
