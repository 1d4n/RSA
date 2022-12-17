from number_theory_functions import modular_exponent

M = 1000
PHI_M = 400
BASE = 456456
E_BASE = 7896543
E_EXP = 74365753

# Hundreds digit of BASE**(E_BASE**E_EXP)

r = modular_exponent(E_BASE, E_EXP, PHI_M)
x = modular_exponent(BASE, r, M)
print(f"({E_BASE}**{E_EXP}) % {PHI_M} = {r}"
      f"\n=> {BASE}**({E_BASE}**{E_EXP}) % {M}"
      f"\n= ({BASE} ** {r}) % {M} = {x}"
      f"\n=> The hundreds digit is: {x // 100}")
