from tools import tools as t


class Query:
    def __init__(self, content):
        self.__dict = {}
        self.Set("", content)

    def Group(self, query, content):
        self.__dict[query] = QueryInit(content)
        return self.__dict[query]

    def Set(self, query, content):
        self.__dict[query] = content

    def Set_All(self, query, content):
        for v in query:
            self.Set(v, content)

    def Analysis(self, query):
        if not self.Contain(query) or query == "":
            return self.__dict[""]
        elif not t.type_name(self.__dict[query], "str"):
            return self.__dict[query]
        return self.__dict[""]

    def Contain(self, query):
        return query in self.__dict

    def __str__(self):
        return str(self.__dict)


def QueryInit(content):
    return Query(content=content)
