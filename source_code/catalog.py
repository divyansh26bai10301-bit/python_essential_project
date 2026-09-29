prods = {
    "APP-01": {"cd": "APP-01", "n": "Apples (1kg)", "cat": "Produce", "pr": 120.0, "stk": 20},
    "MLK-02": {"cd": "MLK-02", "n": "Milk (1L)", "cat": "Dairy", "pr": 60.0, "stk": 25},
    "BRD-03": {"cd": "BRD-03", "n": "Bread Loaf", "cat": "Bakery", "pr": 40.0, "stk": 15},
    "EGG-04": {"cd": "EGG-04", "n": "Eggs (12pk)", "cat": "Dairy", "pr": 90.0, "stk": 12},
    "OAT-05": {"cd": "OAT-05", "n": "Oats (500g)", "cat": "Cereal", "pr": 110.0, "stk": 10}
}

def get_catalog():
    return list(prods.values())

def get_item(cd):
    c = str(cd).strip().upper()
    if c in prods:
        return prods[c]
    return None

def deduct_stock(cd, q):
    i = get_item(cd)
    if i is None:
        return False
    if q <= i["stk"]:
        i["stk"] = i["stk"] - q
        return True
    return False

def do_show_products():
    itms = get_catalog()
    print("\nCode      Name                 Category    Price      Stock")
    print("------------------------------------------------------------------")
    for i in itms:
        print(i["cd"].ljust(10) + i["n"].ljust(21) + i["cat"].ljust(12) + str(i["pr"]).ljust(11) + str(i["stk"]))
    print("\nCoupons: SAVE10 (10% off), GROCERY20 (20% off)")
