from number_theory_functions import extended_gcd

BUYER_COIN_VALUE = 911
SELLER_COIN_VALUE = 7879
PRICE = 1_000_000

# A solution in integers for the equation: BUYER_COIN_VALUE * x + SELLER_COIN_VALUE * y = PRICE

d, a, b = extended_gcd(BUYER_COIN_VALUE, SELLER_COIN_VALUE)
print(f"{BUYER_COIN_VALUE} * ({a}) + {SELLER_COIN_VALUE} * ({b}) = {d}")

if PRICE % d != 0:
    print("NO SOLUTION")
else:
    q = PRICE // d
    # now: q*a * buyer_coin_value + q*b * seller_coin_value = q*d = price
    x, y = q*a, q*b
    print(f"{BUYER_COIN_VALUE}*({x}) + {SELLER_COIN_VALUE}*({y}) = {BUYER_COIN_VALUE*x + SELLER_COIN_VALUE*y:,}"
          f"\n=> {x = }, {y = }")
