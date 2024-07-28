from tools import tools as t


class Query:
    def __init__(self, content: any) -> None:
        self.__dict = dict()
        self.Set("", content)

    def Group(self, query: str, content: any) -> any:
        self.__dict[query] = QueryInit(content)
        return self.__dict[query]

    def Set(self, query: str, content: any) -> None:
        self.__dict[query] = content

    # def Set_All(self, query, content):
    #     for v in query:
    #         self.Set(v, content)

    def Analysis(self, query: str) -> any:
        if not self.Contain(query) or query == "":
            return self.__dict[""]
        elif not t.type_name(self.__dict[query], "str"):
            return self.__dict[query]
        return self.__dict[""]

    def Contain(self, query: str) -> bool:
        return query in self.__dict


def QueryInit(content: any) -> Query:
    return Query(content=content)
