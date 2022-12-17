from number_theory_functions import modular_exponent

e = 11
N = 991
E = lambda x: modular_exponent(x, e, N)

d = dict()
for a in range(N):
    img = E(a)
    if img in d:
        print(f"E is not injective. E({a}) = E({d[img]}) = {img}")
        break
    else:
        d[img] = a
else:  # if we didn't reach the break statement
    print("E is injective.")
