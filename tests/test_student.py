import unittest
from src.student import Student
class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student("favour","igwe","favourigwe@example.com","password")

    def test_registration_is_successful(self):
        result = self.student.register("favour","igwe", "favourigwe@example.com", "password123")
        self.assertTrue(result)

    def test_register_invalid_credentials(self):

        self.student.register("favour","igwe", "favourigwe@example.com", "password123")
        result = self.student.register("favour"," igwe", "favourigwe@example.com", "password456")
        self.assertFalse(result)

    def test_login_is_successful(self):
        self.student.register("favour"," igwe", "favourigwe@example.com", "password123")
        result = self.student.login("favourigwe@example.com", "password123")
        self.assertTrue(result)

    def test_login_invalid_credentials(self):
        self.student.register("favour","igwe", "favourigwe@example.com", "password123")
        result = self.student.login("favourigwe@example.com", "wrongpassword")
        self.assertFalse(result)

    def test_view_enrolled_courses(self):
        self.student.register("favour","igwe", "favourigwe@example.com", "password123")
        self.student.login("favourigwe@example.com", "password123")
        courses = self.student.view_enrolled_courses(1)
        self.assertEqual(courses, [])

    def test_enroll_course(self):
        self.student.register("favour","igwe", "favourigwe@example.com", "password123")
        self.student.login("favourigwe@example.com", "password123")
        result = self.student.enroll_course(101)
        self.assertTrue(result)

    def test_enroll_course_failure_not_logged_in(self):
        self.student.register("favour","igwe ", "favourigwe@example.com", "password123")
        result = self.student.enroll_course(101)
        self.assertFalse(result)

    def test_enroll_course_failure_course_already_enrolled(self):
        self.student.register("favour","igwe", "favourigwe@example.com", "password123")
        self.student.login("favourigwe@example.com", "password123")
        self.student.enroll_course(101)
        result = self.student.enroll_course(101)
        self.assertFalse(result)
