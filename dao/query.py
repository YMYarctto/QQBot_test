from tools import tools as t


class Query:
    def __init__(self, content: any) -> None:
        self.dict = dict()
        self.Set("", content)

    def Group(self, query: str, content: any) -> any:
        self.dict[query] = QueryInit(content)
        return self.dict[query]

    def Set(self, query: str, content: any) -> None:
        self.dict[query] = content

    # def Set_All(self, query, content):
    #     for v in query:
    #         self.Set(v, content)

    def Analysis(self, query: str) -> any:
        if not self.Contain(query) or query == "":
            return self.dict[""]
        elif not t.type_name(self.dict[query], "str"):
            return self.dict[query]
        return self.dict[""]

    def Contain(self, query: str) -> bool:
        return query in self.dict


def QueryInit(content: any) -> Query:
    return Query(content=content)
