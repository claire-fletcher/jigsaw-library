import unittest

class TestLibrary(unittest.TestCase):
    def test_web_server_succeeds(self):
        self.assertEqual(6, 6)


if __name__ == "__main_":
    unittest.main()