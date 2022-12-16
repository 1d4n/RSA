from number_theory_functions import *
import random

def no_digit(num):
    count = 0
    while (num > 0):
        count += 1
        num //= 10
    return count

class RSA():
    def __init__(self, public_key, private_key = None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits = 10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        p = generate_prime(digits//2)
        q = generate_prime(digits//2)
        N = p*q
        
        while(no_digit(N)!= digits):
            p = generate_prime(digits//2)
            q = generate_prime(digits//2)
            N = p*q
        phi_n = (p-1)*(q-1)
        e = random.randint(2, phi_n-1)
        gcd = extended_gcd(phi_n, e)

        # Make sure e is part of U(phi(N))
        while (gcd[0] != 1):
            e = random.randint(2, phi_n -1)
            gcd = extended_gcd(phi_n, e)

        d = modular_inverse(e, phi_n)

        return RSA((N,e), (N, d))


    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        return modular_exponent(m, self.public_key[1], self.public_key[0])


    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        return modular_exponent(c, self.private_key[1], self.private_key[0])