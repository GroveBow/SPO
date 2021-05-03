from pprint import pprint

from Terminal import Terminal
import re
class Lexer:
    def __init__(self):
        self.pattern_terminals = [Terminal("K_WHILE", "while"), Terminal("K_IF", "if"), Terminal("K_ELSE", "else"),
                                  Terminal("VAR", "[a-zA-Zа-яА-Я]+"), Terminal("OP", "[-+*/]"),
                                  Terminal("LBreaket", "[(]"), Terminal("RBreaket", "[)]"), Terminal("LFBreaket", "[{]"),
                                  Terminal("RFBreaket", "[}]")]
        self.list_of_terminals = []

    def get_terminals(self, list_of_tokens):
        for lexem in list_of_tokens:
            lexem_type = self.search_terminal(lexem)
            if lexem_type:
                self.list_of_terminals.append(Terminal(lexem_type, lexem))

    def search_terminal(self, lexem):
        for j in self.pattern_terminals:
            if re.fullmatch(j.value, lexem):
                return j.type
        return 0

    def get_list_of_terminals(self):
        return self.list_of_terminals

    def get_tokens(self, text):
        list_of_tokens = []
        special_characters = ['(', ')', '{', '}']
        math_operations = ['+', '-', '*', '/']
        for line in text.split('\n'):
            left_index = False
            for i in range(len(line)):
                letter = line[i]
                if line[i].isalpha():
                    if not left_index:
                        left_index = i + 1
                elif left_index:
                    list_of_tokens.append(line[left_index - 1:i])
                    left_index = False
                if line[i] in math_operations or line[i] in special_characters:
                    list_of_tokens.append(line[i])
            if left_index:
                list_of_tokens.append(line[left_index - 1:])
        self.get_terminals(list_of_tokens)

        return 0


lex = Lexer()
text = open('kod.txt', 'r', encoding='utf-8').read()
lex.get_tokens(text)
pprint(lex.get_list_of_terminals())
