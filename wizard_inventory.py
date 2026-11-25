
def menu():
    print("Welcome to Wizard Inventory")
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

def show(inventory):
    if len(inventory) == 0:
        print("Your inventory is empty")
    else:
        for i, item in enumerate(inventory, start = 1):
            print(f"{i}. {item}")
    print()

def grab(inventory):
    item = input("Name of item: ")
    inventory.append(item)
    print(f"{item} was added.")
    print()

def edit(inventory):
    item_number = int(input("Number of item: "))
    if item_number < 0 or item_number > len(inventory):
        print("Invalid item number.")
    else:
        updated_name = input("Updated name: ")
        inventory[item_number -1] = updated_name
        print(f"Updated name: {updated_name}")
        print(f"Item number: {item_number} was updated.")
        print()

def drop(inventory):
    if len(inventory) == 0:
        print("Your inventory is empty.")
        return
    item_number = int(input("Item number: "))
    if item_number < 1 or item_number > len(inventory):
        print("Invalid item number")
    else:
        item_name = inventory.pop(item_number -1)
        print(f"{item_name} was dropped.")
    
    

def main():
    inventory = ["wooden staff", "wizard hat", "cloth shoes"]
    while True:
        menu()
        command = input("Command: ")
        if command == "show":
            show(inventory)
        if command == "grab":
            grab(inventory)
        if command == "edit":
            edit(inventory)
        if command == "drop":
            drop(inventory)
        if command == "exit":
            break
    print("Goodbye!")

if __name__ == "__main__":
    main()
