
# kitchen inventory tracker
inventory ={} 
def add_item():
    item = input("enter item name:").lower()
    quantity = int(input("enter  quantity:"))

    inventory[item]=quantity
    print("item added successfully!")

def view_inventory():
    if not inventory:
        print("invent is empty.")
    else:
        print("=======kitchen inventory=====")
    for item, quantity in inventory.items():
        print(f"{item}:{quantity}")

def update_quantity():
    item = input("enter item name:").lower()
    if item in inventory:
        quantity = int(input("enter new quantity:"))
        inventory[item] = quantity
        print("quantity updated successfully!")
    else:
        print("item not found.")

def remove_item():
    item = input("enter  item:").lower()
    if item in inventory:
        del inventory[item]
        print("deleted item succesfully!")
    else:
        print("items not found.")

while True:
    print("\n==========kitchen inventory tracker============")
    print("1. add item")
    print("2. view inventory")
    print("3.update quantity")
    print("4.remove item")

    choice = input("enter a choice:")
    
    if choice == "1":
        add_item()
    elif choice =='2':
        view_inventory()
    elif choice=='3':
        update_quantity()
    elif choice=='4':
        remove_item()
    else:
        print("invalid choice. please try again.")            
