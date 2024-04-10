import unittest

from lib.solutions.CHK.checkout_solution import checkout


class TestCheckOut(unittest.TestCase):
    def test_A_discount(self):
        self.assertEqual(
            checkout("A A A"),
            130,
        )
        self.assertEqual(
            checkout("A A"),
            100,
        )