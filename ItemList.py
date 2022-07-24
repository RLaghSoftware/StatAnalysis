import math

from Item import Item


class ItemList:
    selectedItem = None
    ItemSize = 1
    DefaultName = "Unnamed Item"
    Items = []
    Mean = []
    Median = []
    Mode = []
    SD = []
    ItemA = None

      #initialization
    def __init__(self):
        self.ItemSize = 1

    def __init__(self, size):
        #input validation
        while size is not int:
            try:
                size = int(size)
                break
            except ValueError:
                print('Please enter a valid number for item size')
                size = input(": ")


        self.ItemSize = abs(size)
        i = 1
        while (i<=size):
            self.Mean.append(0.0)
            self.Median.append(0.0)
            self.Mode.append(0.0)
            self.SD.append(0.0)
            i = i +1

    def __init__(self, size, name):
        #input validation
        while size is not int:
            try:
                size = int(size)
                break
            except ValueError:
                print('Please enter a valid number for item size')
                size = input(": ")

        self.ItemSize = abs(size)
        i = 1
        while (i<=size):
            self.Mean.append(0.0)
            self.Median.append(0.0)
            self.Mode.append(0.0)
            self.SD.append(0.0)
            i = i +1
        self.DefaultName = name

    #Adds Items to the list
    def AddItem(self):
        self.ItemA = Item(self.DefaultName, self.ItemSize) #Creates Empty item with correct size
        i = 1
        while (i <= self.ItemSize): #fills Item with user input values
            Inp = input("Enter a value for position "+ str(i) +" in the item, or give no input for None: ")
            if Inp == '' or Inp.isspace():  #enters null value
                self.ItemA.editValue(i,None)
            else:  #input validation
                while (Inp is not int or Inp is not float) and (Inp.isspace() is False and str(Inp) != ''):
                    try:
                        x = Inp
                        Inp = float(Inp)
                        break
                    except ValueError:
                        print('Please enter a valid number:')
                        Inp = input(": ")
                if str(Inp).isspace() or str(Inp) == '':
                    self.ItemA.editValue(i,None)
                else:
                    self.ItemA.editValue(i, Inp) #end of input validation
            i = i + 1 #move to next value within item
        self.Items.append(self.ItemA) #append item to list/ database
        self.selectedItem = self.ItemA #select new item
        self.ItemA = None

        for VALUE in range(self.ItemSize): #calculate stats
            self.findMean( (VALUE+1))
            self.findMedian( (VALUE + 1))
            self.findMode( (VALUE + 1))
            self.findSD( (VALUE + 1))

    #Same as AddItem, but this time name is given
    def AdditemN(self, name):
        self.ItemA = Item(name, self.ItemSize)
        i = 1
        while (i <= self.ItemSize):
            Inp = input("Enter a value for position "+ str(i) +" in the item, or give no input for None: ")
            if Inp == '' or Inp.isspace():
                self.ItemA.editValue(i,None)
            else:
                while (Inp is not int or Inp is not float) and (Inp.isspace() is False and str(Inp) != ''):
                    try:
                        x = Inp
                        Inp = float(Inp)
                        break
                    except ValueError:
                        print('Please enter a valid number:')
                        Inp = input(": ")
                if str(Inp).isspace() or str(Inp) == '':
                    self.ItemA.editValue(i,None)
                else:
                    self.ItemA.editValue(i, Inp)
            i = i + 1
        self.Items.append(self.ItemA)
        self.selectedItem = self.ItemA
        self.ItemA = None

        for VALUE in range(self.ItemSize):
            self.findMean( (VALUE+1))
            self.findMedian( (VALUE + 1))
            self.findMode( (VALUE + 1))
            self.findSD( (VALUE + 1))

    #removes Items from the list
    def RemoveItem(self):
        self.Items.remove(self.selectedItem)

    #selects an item to work with
    def selectItem(self, pos):
        #input validation
        position = pos
        while position.isnumeric() is False or int(position) < 1 or int(position) > len(self.Items):
            print('Please enter a valid number')
            position = input(": ")
        #end input validation
        self.selectedItem = self.Items[int(position)-1]

    # Changes value of selected item, at position c, to "value"
    def EditItem(self, c, value):

        category = c
        while category.isspace() is True or category.isnumeric() is False or int(category) < 1 or int(category) > self.ItemSize:
            print('Please enter a valid number for category')
            category = input(": ")

        if value == '' or value.isspace(): #adds null value
            self.selectedItem.editValue(int(category), None)
            return 0
        else:  #input validation
             while value is not int or value is not float:
                try:
                    v = value
                    value = float(value)
                    break
                except ValueError:
                    if v == '' or v.isspace():
                        self.selectedItem.editValue(int(category), None)
                        return 0
                    print('Please enter a valid number:')
                    value= input(": ") #end input validation
        self.selectedItem.editValue(int(category), value) #edits value of selected item

    #changes name of the selected item
    def ChangeName(self, NewName):

        self.selectedItem.ChangeName(NewName)

    #adds a category to all items, with None as default, but value as default to the selected item
    def addCategory(self, value):
        #input validation
        for _Item_ in self.Items:
            _Item_.addvalue()

        self.ItemSize = self.ItemSize + 1
        while (value is not int or value is not float) and (str(value).isspace() is False and str(value) != ''):
            try:
                value = float(value)
                break
            except ValueError:
                    print('Please enter a valid number:')
                    value = input(": ") #end input validation
        if str(value) == '' or str(value).isspace():
            self.selectedItem.editValue(self.ItemSize, None)
        else:
            self.selectedItem.editValue(self.ItemSize,value)
        #add  values to stat list
        self.Mean.append(0.0)
        self.Median.append(0.0)
        self.Mode.append(0.0)
        self.SD.append(0.0)

        #find stats
        self.findMean( self.ItemSize)
        self.findMedian( self.ItemSize)
        self.findMode( self.ItemSize)
        self.findSD( self.ItemSize)

    #removes an entire category on all items
    def RemoveCategory(self, category):
        #input validation
        while (str(category).isnumeric() is False or int(category) <1 or int(category) > self.ItemSize):
            category = input("Please enter a valid number:")
        #remove Items
        for _Item_ in self.Items:
            _Item_.removevalue(int(category))
        #remove items in stat list
        self.Mean.pop(int(category)-1)
        self.Median.pop(int(category)-1)
        self.Mode.pop(int(category)-1)
        self.SD.pop(int(category)-1)

    #clears entire database
    def Clear(self):
        self.selectedItem = None
        self.ItemSize = 1
        self.DefaultName = "Unnamed Item"
        self. Items = []
        self.Mean = []
        self.Median = []
        self.Mode = []
        self.SD = []
        self.ItemA = None

    #sorts all items, from given category, ascending
    def sortAscending(self, category):
        #input validation
        while (str(category).isnumeric() is False or int(category) < 1 or int(category) > self.ItemSize):
            category = input("Please enter a valid number:")
        self.Items.sort(key=lambda x:x.values[int(category)-1])

    # sorts all items, from given category, descending
    def sortdescending(self, category):
        #input validation
        while (str(category).isnumeric() is False or int(category) < 1 or int(category) > self.ItemSize):
            category = input("Please enter a valid number:")
        self.Items.sort(key=lambda x:x.values[int(category)-1], reverse=True)

    # displays list
    def DisplayList(self):
        for _Item_ in self.Items:
            _Item_.Display()

    #stat calculations
    def findMean (self, category):
        #add relevant values to tracker list
        Tracker = []
        for _Item_ in self.Items:
            if _Item_.GetValueAt(category) is not None:
                Tracker.append(float(_Item_.GetValueAt(category)))
        # mean equation
        sum =0
        count =0

        for value in Tracker:
                sum = sum+float(value)
                count = count+1
        if len(Tracker) == 0:
            Mean = None
        else:
            Mean = sum/count
        self.Mean[category-1] = Mean

    def findMedian (self, category):
        #fill Tracker with relevant values
        Tracker = []
        Median = None
        for _Item_ in self.Items:
            if _Item_.GetValueAt(category) is not None:
                Tracker.append(float(_Item_.GetValueAt(category)))
        if len(Tracker) == 0:
            Median = None
        else:
            Tracker.sort()
            #remove first and last values of sorted tracker to find median
            if ((len(Tracker))%2) == 0:
                while (len(Tracker) >2):
                    Tracker.pop((len(Tracker)-1))
                    Tracker.pop(0)
                Median = (Tracker[0]+Tracker[1])/2
            else:
                while (len(Tracker) >1):
                    Tracker.pop((len(Tracker)-1))
                    Tracker.pop(0)
                Median = Tracker[0]

        self.Median[category - 1] = Median

    def findMode (self, category):
        #fill Tracker with relevant values
        Tracker = []
        for _Item_ in self.Items:
            if _Item_.GetValueAt(category) is not None:
                Tracker.append(float(_Item_.GetValueAt(category)))
        Mode_ = []
        if len(Tracker) == 1:
            Mode_.append(Tracker[0])
        else:
            #sort tracker, change count whenever value changes, whichever value has highest count is mode
            Tracker.sort()
            MaxCount = 1
            Count = 1
            for x in range(len(Tracker)-1):
                if (Tracker[x] == Tracker[x+1]):
                    Count = Count+1

                else:
                    Count = 1

                if Count > MaxCount:
                    MaxCount = Count
                    Mode_ = []
                    Mode_.append(Tracker[x])
                elif Count == MaxCount:
                        Mode_.append(Tracker[x])
        self.Mode[category-1] = Mode_

    def findSD (self, category):
        if self.Mean[category-1] is None:
            SD_ = None
        else:
            #fill tracker with relevant values
            Tracker = []
            for _Item_ in self.Items:
                if _Item_.GetValueAt(category) is not None:
                    Tracker.append(float(_Item_.GetValueAt(category)))
            #SD equation
            M = self.Mean[category-1]
            s=0
            for value in Tracker:
                v = (value - M) * (value - M)
                s = s+v
            X = s/len(Tracker)
            SD_ = math.sqrt(X)

        self.SD[category - 1] = SD_

    def DisplayMean (self):
        for X in self.Mean:
            print(X)

    def DisplayMedian (self):
        for X in self.Median:
            print(X)

    def DisplayMode (self):
        for X in self.Mode:
            print(X)

    def DisplaySD (self):
        for X in self.SD:
            print(X)








