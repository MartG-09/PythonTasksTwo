import unittest

import palindrome_and_prime_number

class TestPalindromeAndPrimeNumber(unittest.TestCase):

    def test_that_palindrome_and_prime_number_exists(self):
        palindrome_and_prime_number.check_if_number_is_palindrome_and_prime(324)

    def test_that_number_isPrime(self):
        number = 72
        is_prime = palindrome_and_prime_number.check_if_number_is_palindrome_and_prime(number)
        self.assertFalse(is_prime)

    def test_that_number_ispalindrome(self):
        number = 121
        is_prime = palindrome_and_prime_number.check_if_number_is_palindrome_and_prime(number)

    def test_that_number_both_palindrome_isPrime(self):
        number = 131
        is_prime = palindrome_and_prime_number.check_if_number_is_palindrome_and_prime(number)
        self.assertTrue(is_prime)
