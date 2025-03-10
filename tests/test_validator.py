import os
import unittest

from exceptions.exception import InvalidNameLengthException, NullException, InvalidEmailPatternException, \
    InvalidPasswordLengthException, InvalidCourseCodeException
from src.validator import Validator
import tempfile


class MyValidatorTestCase(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()

        if os.path.exists('email.txt'):
            os.remove('email.txt')

    def test_both_first_name_and_last_name_is_only_series_of_letters(self):
        first_name = "Favour"
        last_name = "Igwe"
        self.assertEqual(True, self.validator.validate_first_name(first_name))
        self.assertEqual(True, self.validator.validate_last_name(last_name))

    def test_that_when_first_name_is_less_than_four_it_throws_invalid_name_length_exception(self):
        first_name = "Fr"
        last_name = "Igwe"
        with self.assertRaises(InvalidNameLengthException):
            self.validator.validate_first_name(first_name)

    def test_that_when_last_name_is_less_than_four_it_throws_invalid_name_length_exception(self):
        first_name = "Favour"
        last_name = "Ie"
        with self.assertRaises(InvalidNameLengthException):
            self.validator.validate_first_name(last_name)

    def test_that_user_must_input_both_first_name_and_last_name_is_only_series_of_letters(self):
        first_name = "Favour123"
        last_name = "Ig22we"
        with self.assertRaises(InvalidNameLengthException):
            self.validator.validate_first_name(first_name)
            self.validator.validate_last_name(last_name)

    def test_that_user_cannot_leave_either_first_name_and_last_name_blank(self):
        first_name = ""
        last_name = "Igwe"
        with self.assertRaises(NullException):
            self.validator.validate_first_name(first_name)
        first_name1 = "Favour"
        last_name1 = ""
        with self.assertRaises(NullException):
            self.validator.validate_last_name(last_name1)

    def test_that_user_input_the_correct_email_pattern(self):
        self.validator.validate_email("Favour123@gmail.com")
        self.assertTrue(self.validator.validate_email("Favour123@gmail.com"))
        self.validator.validate_email("Favour@semicolon.yahoo.com")
        self.assertTrue(self.validator.validate_email("Favour@semicolon.yahoo.com"))
        self.validator.validate_email("africa@yahoo.org")
        self.assertTrue(self.validator.validate_email("africa@yahoo.org"))

    def test_that_email_field_being_blank_throws_null_exception(self):
        with self.assertRaises(NullException):
            self.validator.validate_email("")

    def test_that_ending_an_email_with_full_stop_would_throw_Invalid_email_exception(self):
        with self.assertRaises(InvalidEmailPatternException):
            self.validator.validate_email("semicolon.yahoo.com.")

    def test_that_password_is_valid(self):
        password = self.validator.validate_password("PASSWORD")
        self.assertTrue(password)

    def test_that_password_is_not_valid(self):
        with self.assertRaises(InvalidPasswordLengthException):
            password = self.validator.validate_password("ORD>")

    def test_that_course_title_is_valid(self):
        title = self.validator.validate_course_title("Introduction to English")
        self.assertTrue(title)

    def test_that_course_code_is_not_valid(self):
        with self.assertRaises(InvalidCourseCodeException):
            self.validator.validate_course_code(",math123")
        with self.assertRaises(InvalidCourseCodeException):
            self.validator.validate_course_code("math 123")

    def test_that_course_code_is_valid(self):
        course = self.validator.validate_course_code("Math123")
        self.assertTrue(course)

    def test_register_email_duplicate(self):
        email = "test@example.com"
        Validator.register_email(email)
        self.assertFalse(self.validator.register_email(email))
        with open("email.txt", 'r') as file:
            emails = [line.strip() for line in file]
            self.assertEqual(emails.count(email), 1)

    def test_register_email_duplicate_two(self):
        email = "Favour@semicolon.com"
        Validator.register_email(email)
        self.assertTrue(self.validator.register_email(email))
        with open("email.txt", 'r') as file:
            emails = [line.strip() for line in file]
            self.assertEqual(emails.count(email), 1)






        


