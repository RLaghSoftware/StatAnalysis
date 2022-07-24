from ItemList import ItemList
from Item import Item

# Ask for Default Size and value

#Create ItemList

#options to: Add Item, Remove Item, Add category, remove cateogry, select Item, edit value, change name,
#options to (cont): clear/exit, sort, Display, Show mean/median/mode/SD

Size = input("Enter the amount of values in an Item: ")
Name = input("Enter a default name for your items: ")

ItemListA = ItemList(Size,Name)


while True:
    print("")
    print("")
    print(
        "Type 0 to add an Item with the default name, Type 1 to add an Item, 2 to remove selected Item, 3 to add"
        " category"
        ", 4 to remove category, 5 to select value, 6 to edit selected value, 7 to change name of selected item, 8 to "
        "sort list ascending, 9 to sort the list descending, and 10 to clear data and exit")
    Option = input(" Type your numeric value:")
    #input validation
    Option = int(Option)
    if Option == 0:
        ItemListA.AddItem()

    elif Option == 1:
        Name = input("Enter the given name")
        ItemListA.AdditemN(Name)

    elif Option == 2:
        ItemListA.RemoveItem()

    elif Option == 3:
        Category = input("Enter a value for the category")
        ItemListA.addCategory(Category)

    elif Option == 4:
        Category = input("Enter the category")
        ItemListA.RemoveCategory()

    elif Option == 5:
        Item = input("Select an Item on the list based on its position on the displayed list (first starts with 1)")
        ItemListA.selectItem(Item)

    elif Option == 6:
        Category = input("Enter the position of the category you want to edit")
        Value = input("Enter the new value, or press enter with no input for None")
        ItemListA.EditItem(Category, Value)

    elif Option == 7:
        Name = input("Enter the new name")
        ItemListA.ChangeName(Name)

    elif Option == 8:
        Category = input("Enter the position of the category you want to sort by")
        ItemListA.sortAscending(Category)

    elif Option == 9:
        Category = input("Enter the position of the category you want to sort by")
        ItemListA.sortdescending(Category)

    elif Option == 10:
        ItemListA.Clear()
        exit(0)
    else:
        print("Error: Invalid option")
    print(" ")
    print("List:")
    ItemListA.DisplayList()
    print("")
    print("Means:")
    ItemListA.DisplayMean()
    print("")
    print("Standard Deviations:")
    ItemListA.DisplaySD()
    print("")
    print("Medians:")
    ItemListA.DisplayMedian()
    print("")
    print("Modes:")
    ItemListA.DisplayMode()














ItemListA.DisplayList()

