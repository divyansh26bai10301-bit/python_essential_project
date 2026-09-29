def get_coupon_rate(c):
    c = str(c).strip().upper()
    if c == "SAVE10":
        return 0.10
    elif c == "GROCERY20":
        return 0.20
    else:
        return 0.0
