from number_theory_functions import is_prime, modular_inverse

e = 11
N = 991

print(f"{is_prime(N) = }")
phi_N = 990
print(f"Inverse of {e} in U_{phi_N} is: {modular_inverse(e, phi_N)}")
