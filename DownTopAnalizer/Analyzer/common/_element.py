class Element:
    name = ''
    Last = []
    First = []
    LastPlus = []
    FirstPlus = []

    def __init__(self, name):
        self.name = name

    def setLast(self, last_list):
        for i in last_list:
            self.Last.append(i)

    def setFirst(self, first_list):
        for i in first_list:
            self.First.append(i)

    def findLastPlus(self):
        for i in self.Last:
            self.LastPlus.append(i)

        for i in self.LastPlus:
            for j in i.Last:
                if not self._is_already_in(item=j, items_list=self.LastPlus):
                    self.LastPlus.append(j)


    def findFirstPlus(self):
        for i in self.First:
            self.FirstPlus.append(i)

        for i in self.FirstPlus:
            for j in i.First:
                if not self._is_already_in(item=j, items_list=self.FirstPlus):
                    self.FirstPlus.append(j)

    @staticmethod
    def _is_already_in(item, items_list):
        for i in  items_list:
            if item.name == i.name:
                return True

        return False