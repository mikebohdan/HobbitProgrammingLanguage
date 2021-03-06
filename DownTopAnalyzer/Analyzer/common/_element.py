class Element:
    name = ''

    def __init__(self, name):
        self.Last = []
        self.First = []
        self.LastPlus = []
        self.FirstPlus = []
        self.Equals = []
        self.name = name

    def setLast(self, last_list):
        for i in last_list:
            self.Last.append(i)

    def setFirst(self, first_list):
        for i in first_list:
            self.First.append(i)

    def findLastPlus(self):
        if self.name[0] != '<' or \
                self.name[-1] != '>':
            return

        for i in self.Last:
            self.LastPlus.append(i)

        for i in self.LastPlus:
            for j in i.Last:
                if not self._is_already_in(item=j, items_list=self.LastPlus):
                    self.LastPlus.append(j)

    def findFirstPlus(self):
        if self.name[0] != '<' or \
                self.name[-1] != '>':
            return

        for i in self.First:
            self.FirstPlus.append(i)

        for i in self.FirstPlus:
            for j in i.First:
                if not self._is_already_in(item=j, items_list=self.FirstPlus):
                    self.FirstPlus.append(j)

    def __str__(self, *args, **kwargs):
        return self.name

    @staticmethod
    def _is_already_in(item, items_list):
        for i in items_list:
            if item.name == i.name:
                return True

        return False

    @staticmethod
    def is_non_terminal(checkable):
        if checkable.name[0] != '<' or \
                checkable.name[-1] != '>':
            return False
        return True