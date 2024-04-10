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

    def test_checkout_G(self):
        self.assertEqual(
            checkout("GG"),
            40,
        )

    def test_checkout_H(self):
        self.assertEqual(
            checkout("HHHHHHHHHH"),
            80,
        )
        self.assertEqual(
            checkout("HHHHHHHHHHHHHHHHHHHH"),
            160,
        )
        self.assertEqual(
            checkout("HHHHHHHH"),
            75,
        )
        self.assertEqual(
            checkout("HH"),
            20,
        )

    def test_checkout_I(self):
        self.assertEqual(
            checkout("II"),
            70,
        )

    def test_checkout_J(self):
        self.assertEqual(
            checkout("JJ"),
            120,
        )

    def test_checkout_K(self):
        self.assertEqual(
            checkout("KKKK"),
            300,
        )
        self.assertEqual(
            checkout("K"),
            80,
        )

    def test_checkout_L(self):
        self.assertEqual(
            checkout("LL"),
            180,
        )

    def test_checkout_M(self):
        self.assertEqual(
            checkout("MM"),
            30,
        )

    def test_checkout_free_item_M(self):
        self.assertEqual(
            checkout("NNNM"),
            120,
        )
        self.assertEqual(
            checkout("NNNMM"),
            135,
        )

    def test_checkout_O(self):
        self.assertEqual(
            checkout("OO"),
            20,
        )

    def test_checkout_P(self):
        self.assertEqual(
            checkout("PPPPP"),
            200,
        )
        self.assertEqual(
            checkout("PPPPPPPPPP"),
            400,
        )
        self.assertEqual(
            checkout("PP"),
            100,
        )

    def test_checkout_Q(self):
        self.assertEqual(
            checkout("QQQ"),
            80,
        )
        self.assertEqual(
            checkout("QQQQQQ"),
            160,
        )
        self.assertEqual(
            checkout("QQ"),
            60,
        )

    def test_checkout_Q_with_free_item(self):
        self.assertEqual(
            checkout("QQQQRRR"),
            230,
        )


    def test_checkout_U(self):
        self.assertEqual(
            checkout("UUUU"),
            120,
        )
        self.assertEqual(
            checkout("UUUUUUUUU"),
            280,
        )

    def test_checkout_V(self):
        self.assertEqual(
            checkout("VVVV"),
            180,
        )
        self.assertEqual(
            checkout("VVVVV"),
            220,
        )
        self.assertEqual(
            checkout("VVVVVV"),
            260,
        )

    def test_checkout_W(self):
        self.assertEqual(
            checkout("WW"),
            40,
        )

    def test_checkout_multi_buy(self):
        self.assertEqual(
            checkout("ZZYS"),
            65
        )


    def test_illegal_input(self):
        self.assertEqual(
            checkout("4"),
            -1,
        )
        self.assertEqual(
            checkout("A90*"),
            -1,
        )

