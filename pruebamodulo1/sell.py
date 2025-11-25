from storage import read_csv, write_csv, save_csv
register_csv = "registersells.csv"
inventory_csv = "inventory.csv"
def register_sell():
    print("Here start the register sold's")
    name_client = str(input("First name of client: ")).lower()
    product_sold = str(input("Product sold: "))
    product_quanty = int(input("quanty of product sold: "))
    date = input("Date today (format: dd/mm/aaaa): ")
    register_s = {
            "client": name_client,
            "product": product_sold,
            "quantity": product_quanty,
            "date": date
        }
    print("sold registered successfully")
    register = read_csv(register_csv)
    register.append(register_s)
    save_csv(register_csv, register)
def list_register():
    register = read_csv(register_csv)
    if not register:
        print("Not product registered")
        return
    
    print("Register product list")
    for r in register:
        register_tuple = (
            r["client"],
            r["product"],
            r["quantity"],
            r["date"]
        )
        print(register_tuple)