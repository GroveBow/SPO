from Token import Token

special_characters = ['(', ')', '{', '}']
math_operations = ['+', '-', '*', '/']

text = open('kod.txt', 'r', encoding='utf-8').read()
list_of_tokens = []

for line in text.split('\n'):
    left_index = False
    for i in range(len(line)):
        letter = line[i]
        if line[i].isalpha():
            if not left_index:
                left_index = i + 1
        elif left_index:
            list_of_tokens.append(Token(line[left_index - 1:i]))
            left_index = False
        if line[i] in math_operations or line[i] in special_characters:
            list_of_tokens.append(Token(line[i]))
    if left_index:
       list_of_tokens.append(Token(line[left_index - 1:]))
    list_of_tokens.append(Token('\n'))

print([i.value for i in list_of_tokens])
