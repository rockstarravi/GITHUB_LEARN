import unittest

from src.python_app import greet


class PythonAppTest(unittest.TestCase):
    def test_greet_returns_expected_message(self):
        self.assertEqual(greet(), "Hello, world")


if __name__ == "__main__":
    unittest.main()
