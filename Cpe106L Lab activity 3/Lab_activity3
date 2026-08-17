class Item:
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty
        if qty > 0:
           self.status = "available"
        else:
           self.status = "Out of stock"
       

class Inventory:
    def __init__(self):
        self.instorage = [] 

    def add_item(self, item):
        self.instorage.append(item)
        print("Item Stored")

    def display_Inventory(self):
        print("Inventory Check:")
        if len(self.instorage) == 0:
            print("No item added")
        else: 
            for item in self.instorage:
                print(f"item: [{item.name}] | Quantity: [{item.qty}] | Status: [{item.status}]")

    def remove_item(self):
        if len(self.instorage) == 0:
            print("\nNo Item Stored")
        else: 
            Search_Item = input("\nEnter name of Item to be removed: ")
            
            for item in self.instorage:
                if Search_Item.upper() == item.name.upper():
                    print("Item found in storage")
                    print(f"Current info: Item: {item.name} | Quantity: {item.qty} | Status: [{item.status}]")
                    self.instorage.remove(item)
                    print("Item Removed") 
                    return
               
            print("\nItem does not exist in database")
    


store = Inventory()
while True:
    print("""
---INVENTORY FILING SYSTEM---
(Select the number for the operation you want to perform)

1 - Add item
2 - Print List of items in inventory
3 - Remove item from inventory
4 - Terminate Program

""")

    action = input("Action(1-4): ")

    #Adds item to iventory
    if action == "1":
        print("\nPlease input the following information:")

        name = input("Enter New Item to be added: ")
        qty = int(input("Quantity of item: "))

        New_item = Item(name, qty)
        store.add_item(New_item)

        print("________________________________________________________________")

    #Displays inventory
    elif action == "2":

        store.display_Inventory()

        print("________________________________________________________________")


    #Search and Remove Students from repository
    elif action == "3":
        store.remove_item()
        print("________________________________________________________________")



    #Terminates the program
    elif action == "4":
        print("\n --TERMINATING PROGRAM --")
        break
        print("________________________________________________________________")

    # Incase the input was invalid
    else:
        print("\nINVALID INPUT, PLEASE TRY AGAIN")