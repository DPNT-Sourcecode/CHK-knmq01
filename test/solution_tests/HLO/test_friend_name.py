import unittest

from lib.solutions.HLO.hello_solution import hello


class TestHello(unittest.TestCase):
    def test_say_hello_friend_name(self):
        self.assertEqual(
            hello("John"),
            "Hello, John!"
        )

