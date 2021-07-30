def make_bold(greet):
    def wrapper(*name):
        text = greet(*name)
        bold = '<b>'
        bold2 = '</b>'
        return bold + text + bold2

    return wrapper
def make_italic(greet):
    def wrapper(*name):
        text = greet(*name)
        italic = '<i>'
        italic2 = '</i>'
        return italic + text + italic2

    return wrapper
def make_underline(greet):
    def wrapper(*name):
        text = greet(*name)
        underline = '<u>'
        underline2 = '</u>'

        return underline + text + underline2

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet('Peter'))

@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f'Hello, {", ".join(args)}'
print(greet_all('Peter','George'))