class Query:
    def __init__(self, content):
        self.__dict = {}
        self.Set("", content)

    def Self(self):
        return self.__dict

    def Set(self, query, content):
        self.__dict[query] = content

    def Analysis(self, query, content):
        if query not in self.__dict:
            return self.__dict[""]
        elif query == "":
            return self.__dict[query]
        else:
            return self.__dict[query].Analysis(content, "")


def QueryInit(content):
    return Query(content=content)
