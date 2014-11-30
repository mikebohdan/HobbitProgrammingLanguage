from tkinter import *
from tokenizer.tokenizer import Tokenizer


class HobbitGUI(Tk):
    def __init__(self, parent=None):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        self.title("Hobbit IDE")

    def initialize(self):
        self.grid()

        spaceTTIF = Label(self)
        spaceTTIF.grid(column=5)
        self.inputField = Text(self)
        self.inputField.grid(column=0, row=0,
                             columnspan=5, rowspan=14, sticky='EW')
        self.tokensTable = Listbox(self, width=100, height=25, font='Courier')
        self.tokensTable.grid(column=6, row=0,
                              columnspan=10, rowspan=14, sticky='EW')
        self.errorsTable = Listbox(self, width=70, height=10, font='Courier')
        self.errorsTable.grid(column=0, row=18, sticky="EW")
        self.inputField.focus_set()

        btnAnalyze = Button(self, text='Click me!',
                     command=self.on_button_parse)
        btnAnalyze.grid(column=0, row=17, columnspan=5)



    def on_button_parse(self):
        self.errorsTable.delete(0)
        source_code = self.inputField.get('1.0', 'end').split('\n')

        # analyzing of input file
        tz = Tokenizer(source_to_analyze=source_code)
        try:
            tz = tz.analyze()
        except Exception as e:
            self.errorsTable.insert(END, e)

        for token in tz['tokens']:
            self.tokensTable.insert(END, token)

    def on_button_analyze(self):
        self.inputField.focus_set()

if __name__ == '__main__':
    app = HobbitGUI()
    app.mainloop()