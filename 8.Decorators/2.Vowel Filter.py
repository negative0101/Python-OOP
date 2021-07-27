def vowel_filter(function):
    def wrapper():
        text = function()
        return [el.lower() for el in text if el in 'aeiouy']
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())