from random import randrange


def powers_of_pow_of_2(a, d, n):
    """
    Returns the powers: a modulo n, by powers of 2 from 2**0 to 2**d
    Parameters
    ----------
    a : The exponential's base.
    d : The last exponential's exponent to raise the base by 2**d.
    n : The exponential's modulus.

    Returns
    -------
    A list of all the powers: (a**i % n), i in {2**0, 2**1, ..., 2**d}.
    """
    result = [a % n]
    for _ in range(1, d):
        result.append(result[-1] ** 2 % n)
    return result


def extended_gcd(a, b):
    """
    Returns the extended gcd of a and b

    Parameters
    ----------
    a : Input data.
    b : Input data.
    Returns
    -------
    (d, x, y): d = gcd(a,b) = a*x + b*y
    """
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


def modular_inverse(a, n):
    """
    Returns the inverse of a modulo n if one exists

    Parameters
    ----------
    a : Input data.
    n : Input data.

    Returns
    -------
    x: such that (a*x % n) == 1 and 0 <= x < n if one exists, else None
    """
    euclid = extended_gcd(a, n)
    if euclid[0] == 1:
        inverse = euclid[1]
        if inverse < 0:
            inverse += n
        return inverse
    return None


def modular_exponent(a, d, n):
    """
    Returns a to the power of d modulo n

    Parameters
    ----------
    a : The exponential's base.
    d : The exponential's exponent.
    n : The exponential's modulus.

    Returns
    -------
    b: such that b == (a**d) % n
    """
    rev_bin_exponent = format(d, 'b')[::-1]
    powers_arr = powers_of_pow_of_2(a, len(rev_bin_exponent), n)
    first_pow = rev_bin_exponent.find('1')
    if first_pow == -1:
        return 0
    a = powers_arr[first_pow]
    for i in range(first_pow + 1, len(rev_bin_exponent)):
        if rev_bin_exponent[i] == '1':
            a *= powers_arr[i]
            a %= n
    return a


def miller_rabin(n):
    """
    Checks the primality of n using the Miller-Rabin test

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a 3/4 chance at least to be False
    """
    a = randrange(1, n)
    k = 0
    d = n - 1
    while d % 2 == 0:
        k = k + 1
        d = d // 2
    x = modular_exponent(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(k):
        x = (x * x) % n
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False


def is_prime(n):
    """
    Checks the primality of n

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a chance of less than 1e-10 to be True
    """
    for _ in range(10):
        if not miller_rabin(n):
            return False
    return True


def generate_prime(digits):
    for i in range(digits * 10):
        n = randrange(10 ** (digits - 1), 10 ** digits)
        if is_prime(n):
            return n
    return None
