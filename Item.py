class Item:

    def __init__(self):
        self.name = ""
        self.values = [0.0]

    def __init__(self, name):
        self.name = name
        self.values = [0.0]

    def __init__(self,name, amount):
        self.name = name
        self.values = [0.0]

        i = 1
        while (i<amount):
            self.values.append(0.0)
            i = i +1


    def addvalue(self):
        #self.values.append(0.0)
        self.values.append(None)

    def removevalue(self, position):
        #input validation
        self.values.pop(position-1)

    def editValue(self, position, value):
        if (len(self.values) < position) or (position < 1):
            print("invalid position")

        else:
            self.values[position-1] = value

    def ChangeName(self, name):
        self.name = name

    def Display(self):
        print(self.name)
        print(self.values)

    def GetValueAt(self, category):
        #input validation
        return self.values[category-1]











