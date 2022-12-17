from rsa_functions import RSA
from number_theory_functions import *
import random

p = 7919
q = 6841
N = p*q
phi_n = (p-1)*(q-1)

e = random.randint(2, phi_n-1)
gcd = extended_gcd(phi_n, e)
# Make sure e is part of U(phi(N))
while (gcd[0] != 1):
    e = random.randint(2, phi_n -1)
    gcd = extended_gcd(phi_n, e)

d = modular_inverse(e, phi_n)
rsa = RSA((N,e), (N, d))

M = 64
encrypted  = rsa.encrypt(M)
print(rsa.public_key)
print ("encrypted:", encrypted)
print(rsa.decrypt(encrypted))