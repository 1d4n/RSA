from rsa_functions import RSA
from number_theory_functions import *
import random

p = 3491
q = 3499

e = 3499

d = modular_inverse(e, (p-1)*(q-1))
print(d)
print(modular_exponent(42, d, 12215009))