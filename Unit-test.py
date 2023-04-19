import unittest
from hello import say_hello

class TestHello(unittest.TestCase):

    def test_say_hello(self):
        self.assertEqual(say_hello(), "hello world!")

    def test_say_hello_uppercase(self):
        self.assertEqual(say_hello().upper(), "HELLO WORLD!")

    def test_say_hello_not_empty(self):
        self.assertTrue(say_hello())

