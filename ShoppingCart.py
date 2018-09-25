shopping_lists = []
list_count = 1
item_count = 1

class ShoppingList():
    def __init__(self, name):
        self.name = name
        self.items = []
        self.id = str(list_count)

    def __repr__(self):
        return ("%s shopping list: %s \n list id : %s") % (self.name, self.items, self.id)

class GroceryItem:
    def __init__(self,item,description):
        self.item = item
        self.description = description
        self.id = str(item_count)
     def __repr__(self):
         return ("%s Grocery Items : %s \n list id : %s") % (self.name, self.items, self.id)

    # def add_item(self,item,price):
    #     self.items.append(ShoppingList)
    #
    # def display_shoppinglist(self):
    #     print(self.items)

while True:
    grocery_input = input("please select: 'V' to view lists, 'Q' to quit, 'A' to add items, 'L' to create new list: ")
    if (grocery_input == "V"):
        for list in shopping_lists:
            print(list)
    elif (grocery_input == "Q"):
        print("Thanks for shopping with us")
        break
    elif (grocery_input == "A"):
        list_id = str(input("Enter the id of the list to add items to: "))
        for list in shopping_lists:
            if list.id == list_id:
                item_name = input("Name of item to add: ")
                item_description = input("Enter description: ")
                new_item = GroceryItem(item_name, item_description)
                list.items.append(new_item)
                item_count += 1
    elif grocery_input == "L":
        name_of_list = input("Name of new list: ")
        new_list = ShoppingList(name_of_list)
        shopping_lists.append(new_list)
        list_count += 1
