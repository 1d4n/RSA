from number_theory_functions import *
import random


class RSA():
    def __init__(self, public_key, private_key=None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits=10):
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
        while True:
            p = generate_prime((digits + 1) // 2)
            q = generate_prime(digits // 2)
            # Make sure p and q have been successfully generated, and they are different
            # and the number of digits of p*q is valid.
            if p and q and p != q and len(str(p * q)) == digits:
                break
        N = p * q
        phi_N = (p - 1) * (q - 1)

        while True:
            e = random.randint(2, phi_N - 1)
            # Make sure e is part of U(phi(N))
            if extended_gcd(phi_N, e)[0] == 1:
                break

        d = modular_inverse(e, phi_N)
        return RSA((N, e), (N, d))

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
