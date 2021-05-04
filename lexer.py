from pprint import pprint

from Terminal import Terminal
import re


class Lexer:
    def __init__(self):
        self.pattern_terminals = [Terminal("K_WHILE", "while"), Terminal("K_IF", "if"), Terminal("K_ELSE", "else"),
                                  Terminal("VAR", "[a-zA-Zа-яА-Я]+"), Terminal("OP", "[-+*/]"),
                                  Terminal("LBreaket", "[(]"), Terminal("RBreaket", "[)]"),
                                  Terminal("LFBreaket", "[{]"),
                                  Terminal("RFBreaket", "[}]"), Terminal("WS", r"\s+")]
        self.list_of_terminals = []


    def search_terminal(self, lexem):
        for j in self.pattern_terminals:
            if re.fullmatch(j.value, lexem):
                return j.type
        return 0

    def get_list_of_terminals(self):
        return self.list_of_terminals

    def get_terminals(self, text):
        lexem = ''
        for i in text:
            letter = i
            lexem += i
            if self.search_terminal(lexem):
                pass
            else:
                self.list_of_terminals.append(Terminal(self.search_terminal(lexem[:-1]), lexem[:-1]))
                lexem = lexem[-1]
        if not lexem == '':
            self.list_of_terminals.append(Terminal(self.search_terminal(lexem), f'{lexem}'))


lex = Lexer()
text = open('kod.txt', 'r', encoding='utf-8').read()
lex.get_terminals(text)
pprint(lex.get_list_of_terminals())
