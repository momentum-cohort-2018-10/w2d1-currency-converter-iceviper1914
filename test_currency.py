from currency import convert


def test_convert_same_currency():
    assert convert([], 1, from_currency= "USD", to_currency="EUR") == 1
    assert convert([], 2, from_currency= "USD", to_currency="EUR") == 2 

def test_convert_usd_to_euros()
    assert convert(rates=[("USD", "EUR", 0.74)]), value=1, current="USD", to="EUR") ==0.74
    assert round(convert(rates=[("USD", "EUR", 0.74)], value=3, current= "USD", to="EUR"), 2)== 2.22

def test_convert_reverse()
    assert round(convert(rates=[("USD", "EUR", 0.74)], value=1, current="EUR", to="USD"), 2) == 1.35

def test_convert_multiple_rates():
    rates = []