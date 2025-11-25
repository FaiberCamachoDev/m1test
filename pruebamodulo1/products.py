from storage import read_csv, write_csv, save_csv
products_csv = "inventory.csv"
def generate_id():
    product = read_csv(products_csv)
    if not product:
        return 1
    used_ids = {int(p["id"]) for p in product}
    new_id = 1
    while new_id in used_ids:
        new_id+=1
    return new_id
def register_product():
    validation_name = True
    validation_price = True
    validation_quanty = True
    validation_category = True
    new_id = generate_id()
    #Enter message
    print("""
    --------------------------------------------
        Let's start to insert your products
    --------------------------------------------
    """)


    while validation_name:
        #request name of product
        product_name = input("Insert the name of the product: ")
        #Is allow the use of numbers and letters for productos like H20
        if product_name.isalnum():
            validation_name = False
        #return to the cycle until the name get correct.
        else:
            print("Don't use Special Characters or Spaces, Try Again.")

    while validation_price:
        #request the price of the product
        product_price = float(input("Cost product: "))

        if product_price > 0:
            validation_price = False
        
        else:
            print("Just positive numbers allowed, Try Again")

    while validation_quanty:
        #Request quanty of product
        product_quanty = int(input("Quanty of product: "))

        if product_quanty > 0:
            validation_quanty = False
        else:
            print("Just integer number allowed")
    while validation_category:
        #request category of product
        product_category = input("Insert the category of the product: ")
        #Is allow the use of numbers and letters for categories
        if product_category.isalnum():
            validation_category = False
        #return to the cycle until the val get correct.
        else:
            print("Don't use Special Characters or Spaces, Try Again.")

    #reserv total cost of the product here
    total_cost = product_price * product_quanty
    product_a ={
        "id": new_id,
        "product": product_name,
        "price": product_price,
        "quantity": product_quanty,
        "category": product_category
    }
    print("\n" + "="*15)
    print("Product Info")
    print("="*15)
    print(f"Name: {product_name} | Price: {product_price} | Quanty: {product_quanty} | Total cost: {total_cost}")
    product=read_csv(products_csv)
    product.append(product_a)
    save_csv(products_csv, product)
def search_product_id():
    search_id = input("Insert product ID: ")
    product = read_csv(products_csv)
    if not product:
        print("No product registered with this ID")
        return
    found = None
    for p in product:
        if str(p["id"]) == search_id:
            found = p
            break
    if found:
        print("------Data Product------")
        print(f"""
ID: {found['id']}
Product: {found['product']}
Price: {found['price']}
Quantity: {found['quantity']}
    """)
    else:
        print("No product registered with this ID")
def delete_product():
    product = read_csv(products_csv)

    if not product:
        print("No product records found.")
        return

    try:
        target_id = int(input("Enter product ID to delete: "))
    except ValueError:
        print("Invalid ID format.")
        return

    # search product and delete it
    new_list = []
    found = False

    for p in product:
        if int(p["id"]) == target_id:
            found = True
            print(f"Product with ID {target_id} deleted successfully.")
            continue  # No added to new list
        new_list.append(p)

    if not found:
        print("Visitor ID not found.")
        return

    # Save new list
    save_csv(products_csv, new_list)
    print("CSV updated successfully.")
def list_product():
    product = read_csv(products_csv)
    if not product:
        print("Not product registered")
        return
    
    print("Visitor list")
    for p in product:
        product_tuple = (
            int(p["id"]),
            p["product"],
            p["price"],
            p["quantity"],
            p["category"],
        )
        print(product_tuple)
def update_stock():
    product = read_csv(products_csv)
    if not product:
        print("No product data found")
        return
    val_target = True
    while val_target:
        target_id = input("Enter product ID for update stock: ")
        if not target_id.isdigit():
            print("Insert a valid ID.")
            continue
        else:
            val_target = False
    target_id = int(target_id)
    found = False
    
    for p in product:
        new_stock = int(input("Insert the new stock of product: "))
        if int(p["id"]) == target_id:
            found = True
            print(f"Current stock of {target_id} ID: {p["quantity"]}")
            if p["quantity"] == new_stock:
                p["quantity"] = new_stock
                print("stock changed successfully")
            else:
                p["quantity"] = new_stock
                print("stock changed successfully")
            break
    if not found:
        print("No ID founded")
        return
    save_csv(products_csv, product)