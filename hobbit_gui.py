#!/usr/bin/env python3

from tkinter import *
import traceback
from tokenizer.tokenizer import Tokenizer
from syntax_analizer.syntax_analyzer import *
from Automat import syntax_analyser


class HobbitGUI(Tk):
    def __init__(self, parent=None):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        self.title("Hobbit IDE")
        self.tz = None

    def initialize(self):
        self.grid()

        spaceTTIF = Label(self)
        spaceTTIF.grid(column=5)
        self.inputField = Text(self)
        self.inputField.grid(column=0, row=0,
                             columnspan=5, rowspan=14, sticky='EW')

        self.tokensTable = Listbox(self, width=100, height=15, font='Courier')
        self.tokensTable.grid(column=6, row=0,
                              columnspan=10, rowspan=10, sticky='EW')
        self.variableTable = Listbox(self, width=100, height=10, font='Courier')
        self.variableTable.grid(column=6, row=10,
                              columnspan=10, rowspan=7, sticky='EW')
        self.constantTable = Listbox(self, width=100, height=10, font='Courier')
        self.constantTable.grid(column=6, row=17,
                              columnspan=10, rowspan=7, sticky='EW')

        self.errorsTable = Listbox(self, width=70, height=10, font='Courier')
        self.errorsTable.grid(column=0, row=18, columnspan=5, sticky="EW")
        self.inputField.focus_set()

        btnParse = Button(self, text="Parse",
                          command=self.on_button_parse)
        btnParse.grid(column=3, row=17)

        btnAnalyze = Button(self, text='Analyze',
                            command=self.analyze)
        btnAnalyze.grid(column=2, row=17)

        btnAnalyze2 = Button(self, text='Analyze2',
                             command=self.analyze2)
        btnAnalyze2.grid(column=1, row=17)

    def test(self):
        source_code = self.inputField.get('1.0', 'end').split('\n')
        for i in source_code:
            print(i)

    def analyze(self):
        if self.tz is None:
            self.errorsTable.insert(END, "No data to analyze.")
        try:
            a = SyntaxAnalyzer(self.tz)
            a.analyze()
            self.errorsTable.insert(END, 'OK')
        except Exception as e:
            for i in e.__str__().split('\n'):
                self.errorsTable.insert(END, i)

    def analyze2(self):
        if self.tz is None:
            self.errorsTable.insert(END, "No data to analyze.")
        else:
            __analyze_input = []
            for i in self.tz['tokens']:
                __analyze_input.append(i.toDict())
            __analyze_output = syntax_analyser.move(__analyze_input)
            for i in __analyze_output:
                self.errorsTable.insert(END, i)

    def on_button_parse(self):
        self.tz = None
        self.tokensTable.delete(0, END)
        self.variableTable.delete(0, END)
        self.constantTable.delete(0, END)
        self.errorsTable.delete(0, END)
        source_code = self.inputField.get('1.0', 'end').split('\n')

        for i in range(len(source_code)):
            source_code[i] += '\n'

        # analyzing of input file
        self.tz = Tokenizer(source_to_analyze=source_code)
        try:
            self.tz = self.tz.analyze()
            self.errorsTable.insert(END, "OK")
        except IndexError:
            pass
        except Exception as e:
            self.errorsTable.insert(END, e)

        for token in self.tz['tokens']:
            self.tokensTable.insert(END, token)

        for i in self.tz['variables']:
            self.variableTable.insert(END, i)

        for i in self.tz['constants']:
            self.constantTable.insert(END, i)

if __name__ == '__main__':
    app = HobbitGUI()
    app.mainloop()