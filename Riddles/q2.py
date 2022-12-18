from number_theory_functions import modular_exponent


BASE = 456456
E_BASE = 7896543
E_EXP = 74365753
# Hundreds digit of BASE**(E_BASE**E_EXP)

n = 1000
phi_n = 400

r = modular_exponent(E_BASE, E_EXP, phi_n)
x = modular_exponent(BASE, r, n)
print(f"({E_BASE}**{E_EXP}) % {phi_n} = {r}"
      f"\n=> {BASE}**({E_BASE}**{E_EXP}) % {n}"
      f"\n= ({BASE} ** {r}) % {n} = {x}"
      f"\n=> The hundreds digit is: {x // 100}")
