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

    def test_B_discount(self):
        self.assertEqual(
            checkout("B B"),
            45,
        )
        self.assertEqual(
            checkout("B"),
            30,
        )

    def test_checkout_multiple_products(self):
        self.assertEqual(
            checkout("A B C D"),
            115,
        )

    def test_illegal_input(self):
        self.assertEqual(
            checkout("Z"),
            -1,
        )
        self.assertEqual(
            checkout("A Z"),
            -1,
        )