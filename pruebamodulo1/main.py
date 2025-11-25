from products import (
    update_stock,
    register_product,
    search_product_id,
    delete_product,
    list_product
)
from sell import (
    list_register,
    register_sell
)
from stats import (
    total_sold
)
def menu_product():

    while True:
        print("""Select an option
1. Register a new product
2. Search product by ID    
3. delete product by ID
4. Show inventory list
5. Update product stock by ID
6. Back to main menu
""")
        op = int(input("> "))
        match op:
            case 1:
                register_product()
            case 2:
                search_product_id()
            case 3:
                delete_product()
            case 4:
                list_product()
            case 5:
                update_stock()
            case 6:
                return
            case _:
                print("Invalid option")
def menu_registered():
    while True:
        print("""\nSelect an option
1. Register a new sold
2. consultation register    
3. Back to main menu
""")
        op = int(input("> "))
        match op:
            case 1:
                register_sell()
            case 2:
                list_register()
            case 3:
                return
            case _:
                print("Invalid option")
def menu_stats():
    while True:
        print("""
-----------Choose an option---------
1. Show top 3 sold's
2. Total sold's
3. calculate income
4. Back to Main menu
""")
        op = int(input(">"))
        match op:
            case 1:
                pass
            case 2:
                total_sold()
            case 3:
                pass
            case 4:
                return
            case _:
                print("Select an valid option")

def main_menu():
    menu = True
    while menu:
        print("""
-----------Choose an option---------
1. Inventory module
2. Register/Consult sells module
3. Reports Module
4. Exit
""")
        op = int(input(">"))
        match op:
            case 1:
                menu_product()
            case 2:
                menu_registered()
            case 3:
                menu_stats()
            case 4:
                print("Leaving the system")
                menu = False
            case _:
                print("Select an valid option")
                continue
main_menu()

