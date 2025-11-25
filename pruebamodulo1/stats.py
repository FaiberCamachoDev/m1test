from storage import save_csv, write_csv, read_csv
stats_csv = "registersells.csv"
# def top_sold():
#     stat = read_csv(stats_csv)
#     for i in stat:
#         top3 = stat
#         pass
def total_sold():
    stat = read_csv(stats_csv)
    if not stat:
        print("Not data found")
        return
    print("-----stats-----")
    total = len(stat)
    print(f"total sold's registered: {total}")
    product_count = {}
    for p in stat:
        product = p["product"].lower()
        product_q = p["quantity"]
        quantity = product_q
        product_count[product] = product_count.get(product, quantity) 

    for i, count in product_count.items():
        print(f" {i}: {count}")
# def income():
#     stat = read_csv(stats_csv)
