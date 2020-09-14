import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for 'primes.py'"""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

    def test_is_four_non_prime(self):
        """Is four correctly determined not to be prime?"""
        self.assertFalse(is_prime(4), msg="Four is not prime!")
    
    def test_is_zero_not_prime(self):
        """Is zero correctly determined not to be prime?"""
        self.assertFalse(is_prime(0))

    def test_negative_number(self):
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index), msg=f'{index} should not be determined to be prime')


if __name__ == '__main__':
    unittest.main()