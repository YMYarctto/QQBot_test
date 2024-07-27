def content_filter(content):
    str_list = content.split()
    return str_list


def type_name(a, t):
    return type(a).__name__ == t
