# rates = [("USD", "EUR", 0.74),("EUR", "JPY", 145.949),("EUR", "GBP", 0.88)]



# value = float(input("What number would you like to convert?"))
# from_currency = "USD"   
# to_currency = "EUR"


# def convert_rates(rates, value, from_currency, to_currency):
#     """This function is going to convert a value from one currency to another"""
#     converted_value = value * 0.74
#     print(converted_value)
#     return converted_value

# convert_rates(rates, 10, from_currency, to_currency)


def convert(rates, value, current, to)
    if current == to:
        return value

    # rates = [("USD,"EUR", 0.74)], ("EUR", "JPY", 100)]
    for conversion in rates
    # conversion = ("USD", "EUR, 0.74")
    if current == conversion[0] and to == conversion[1]:0
        return value * conversion[2]
    if current == conversion[1] and to == conversion[0]:
        return value / conversion[2]
    raise ValueError(f"can't convert from {current} to {to}")

