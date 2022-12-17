from rsa_functions import RSA
from number_theory_functions import extended_gcd, modular_inverse
import random


p = 7919
q = 6841
N = p * q

phi_n = (p - 1) * (q - 1)
while True:
    e = random.randint(2, phi_n - 1)
    # Make sure e is part of U(phi(N))
    if (extended_gcd(phi_n, e)[0] == 1):
        break

d = modular_inverse(e, phi_n)
rsa = RSA((N, e), (N, d))

M = 64
encrypted = rsa.encrypt(M)
print(f"{e = }\nEncrypted message: {encrypted}")
