from number_theory_functions import modular_inverse
from rsa_functions import RSA


e = 3499
p = 3491
q = 3499
N = p * q
M = 42

phi_n = (p-1) * (q-1)
d = modular_inverse(e, phi_n)
print(f"Inverse of {e} in U_{phi_n} is: {d}")
rsa = RSA((N, e), (N, d))
decrypted = rsa.decrypt(M)
print("=> The decrypted message is:", decrypted)
