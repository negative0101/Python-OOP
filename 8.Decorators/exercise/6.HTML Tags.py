def tags(f):
    def text(t):
        def wrapper(*args):
            html_tag = '<' + f + '>'
            html_tag_close = '</' + f + '>'
            return html_tag + t(*args) + html_tag_close
        return wrapper
    return text


@tags("p")
def join_strings(*args):
    return ", ".join(args)


print(join_strings("Hello", "you!"))
