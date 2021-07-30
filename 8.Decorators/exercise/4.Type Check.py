def type_check(t):
    def check_accept(f):
        def wrapper(arg):
            type_of_arg = t
            result = f(arg)
            if type(arg) == type_of_arg:
                return result
            return 'Bad type'
        return wrapper
    return check_accept


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]
print(first_letter(f'Hello World'))
print(first_letter(['Not', 'A', 'String']))