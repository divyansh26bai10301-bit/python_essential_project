from catalog import get_item, deduct_stock
from billing import do_process_bill

cnt = 1001

def do_order():
    global cnt
    inv = "INV-" + str(cnt)
    cnt = cnt + 1
    itms = []

    print("\nStarting new sale: " + inv)

    while True:
        cd = input("\nEnter Product Code (e.g. APP-01): ").strip().upper()
        i = get_item(cd)
        if i is None:
            print("Error: Product not found.")
        else:
            q_str = input("Enter Quantity: ").strip()
            if not q_str.isdigit():
                print("Error: Quantity must be a number.")
            else:
                q = int(q_str)
                if q <= 0:
                    print("Error: Quantity must be at least 1.")
                else:
                    curr_in_order = 0
                    for x in itms:
                        if x["cd"] == i["cd"]:
                            curr_in_order = curr_in_order + x["q"]
                    if (curr_in_order + q) > i["stk"]:
                        print("Error: Not enough stock. Available: " + str(i["stk"] - curr_in_order))
                    else:
                        u_pr = float(i["pr"])
                        t_pr = round(u_pr * q, 2)
                        o_itm = {
                            "cd": i["cd"],
                            "n": i["n"],
                            "q": q,
                            "u_pr": u_pr,
                            "t_pr": t_pr
                        }
                        itms.append(o_itm)
                        print("Added " + str(q) + "x " + i["n"] + " (Rs. " + str(t_pr) + ")")

        m = input("\nDo you want to add another item? (y/n): ").strip().lower()
        if m != "y" and m != "yes":
            break

    if len(itms) == 0:
        print("No items in sale. Order cancelled.")
        return

    cpn = input("\nEnter Coupon Code (SAVE10, GROCERY20 or press Enter to skip): ").strip().upper()
    if cpn == "":
        cpn = "NONE"

    for x in itms:
        deduct_stock(x["cd"], x["q"])

    do_process_bill(inv, itms, cpn)
