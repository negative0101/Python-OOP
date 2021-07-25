def reverse_text(text):
    current_index = len(text) -1
    while current_index >= 0:
        yield text[current_index]
        current_index-= 1


print(reverse_text('step'))
for char in reverse_text('step'):
    print(char,end='')