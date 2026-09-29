from discounts import get_coupon_rate

last_b = None

def calc_bill(itms, cpn):
    sub = 0.0
    for i in itms:
        sub = sub + i["t_pr"]
    sub = round(sub, 2)
    rate = get_coupon_rate(cpn)
    disc = round(sub * rate, 2)
    after = sub - disc
    if after < 0:
        after = 0.0
    tax = round(after * 0.05, 2)
    gtot = round(after + tax, 2)
    return {
        "sub": sub,
        "rate": rate,
        "disc": disc,
        "tax": tax,
        "gtot": gtot,
        "cpn": str(cpn).strip().upper()
    }

def print_receipt(inv, itms, b):
    l = []
    l.append("==================================================")
    l.append("              FRESHMART GROCERY STORE             ")
    l.append("                    TAX INVOICE                   ")
    l.append("==================================================")
    l.append("Invoice No : " + str(inv))
    l.append("--------------------------------------------------")
    l.append("Item Name               Qty   Price      Total")
    l.append("--------------------------------------------------")
    for i in itms:
        l.append(i["n"].ljust(24) + str(i["q"]).ljust(6) + str(i["u_pr"]).ljust(11) + str(i["t_pr"]))
    l.append("--------------------------------------------------")
    l.append("Subtotal      : Rs. " + str(b["sub"]))
    if b["disc"] > 0:
        l.append("Discount (" + b["cpn"] + ") : -Rs. " + str(b["disc"]))
    l.append("Tax (GST 5%)  : Rs. " + str(b["tax"]))
    l.append("==================================================")
    l.append("GRAND TOTAL   : Rs. " + str(b["gtot"]))
    l.append("==================================================")
    l.append("             Thank you for shopping!              ")
    l.append("==================================================")
    print("\n" + "\n".join(l))

def do_process_bill(inv, itms, cpn):
    global last_b
    b = calc_bill(itms, cpn)
    print_receipt(inv, itms, b)
    last_b = (inv, itms, b)

def do_view_last_bill():
    if last_b is None:
        print("\nNo bill generated yet.")
        return
    inv, itms, b = last_b
    print_receipt(inv, itms, b)
