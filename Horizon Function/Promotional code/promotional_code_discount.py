def get_discounted_price(item , price , promo_code):
    code = promo_code.strip()
    promo = code.upper()
    if (price >= 0):
    
        if(promo == "SAVE10"):
            discount = price * 0.1
            new_price = price - discount

        elif(promo == "HALFOFF"):
            discount = price * 0.5
            new_price = price - discount

        else:
            new_price = price

    else:
        raise ValueError ("Price is below 0")
    
    return new_price

