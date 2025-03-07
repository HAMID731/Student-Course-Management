import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        course = Course("Math103", "Mathematics")

    def test_that_couse_can_be_added(self):


if __name__ == '__main__':
    unittest.main()
