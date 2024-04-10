import unittest

from lib.solutions.CHK.checkout_solution import checkout


class TestCheckOut(unittest.TestCase):
    def test_A_discount(self):
        self.assertEqual(
            checkout("AAA"),
            130,
        )
        self.assertEqual(
            checkout("AAAAA"),
            200,
        )
        self.assertEqual(
            checkout("AAAAAAAAA"),
            380,
        )
        self.assertEqual(
            checkout("AA"),
            100,
        )
        self.assertEqual(
            checkout("AAAAAAAAAA"),
            400,
        )

    def test_B_discount(self):
        self.assertEqual(
            checkout("BB"),
            45,
        )
        self.assertEqual(
            checkout("B"),
            30,
        )
        self.assertEqual(
            checkout("BBBB"),
            90,
        )

    def test_free_item_for_B(self):
        self.assertEqual(
            checkout("BEE"),
            80,
        )
        self.assertEqual(
            checkout("BBBEE"),
            125,
        )

    def test_checkout_multiple_products(self):
        self.assertEqual(
            checkout("ABCD"),
            115,
        )
        self.assertEqual(
            checkout("ABCDECBAABCABBAAAEEAA"),
            665
        )
        self.assertEqual(
            checkout("ABCDECBAABCABBAAAEEAAFFF"),
            685
        )

    def test_checkout_F(self):
        self.assertEqual(
            checkout("FFF"),
            20,
        )
        self.assertEqual(
            checkout("FF"),
            20,
        )

    def test_illegal_input(self):
        self.assertEqual(
            checkout("Z"),
            -1,
        )
        self.assertEqual(
            checkout("AZ"),
            -1,
        )
