import unittest

from exceptions.exception import InvalidNameException, InvalidNameLengthException
from src.course import Course


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.course = Course("Math103", "Mathematics")

    def test_that_couse_can_be_added(self):
        self.course.add_student("Ayomide Tayo")
        number = self.course.get_number_of_enrolled_students()
        self.assertEqual(number, 1)
        self.course.add_student("Alayo Pelu")
        number = self.course.get_number_of_enrolled_students()
        self.assertEqual(number, 2)

    def test_that_student_can_be_removed(self):
        self.course.add_student("Ayomide Tayo")
        number = self.course.get_number_of_enrolled_students()
        self.assertEqual(number, 1)
        remove = self.course.remove_student("Ayomide Tayo")
        self.assertEqual(remove, True)
        number = self.course.get_number_of_enrolled_students()
        self.assertEqual(number, 0)

    def test_that_blank_last_name_field_throws_invalid_name_exception(self):
        with self.assertRaises(InvalidNameLengthException):
            self.course.add_student("Ayomide")





if __name__ == '__main__':
    unittest.main()
