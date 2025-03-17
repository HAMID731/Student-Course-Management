import unittest
from src.student import Student
from src.course import Course
from exceptions.exception import InvalidEmailPatternException, InvalidPasswordLengthException

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student1 = Student('Abari', 'Hamid', 'Abariwonda4@gmail.com', 'hamid123')
        self.student2 = Student('favour', 'igwe', 'favor123@gmail.com', 'favour123')
        self.student3 = Student('abimbola', 'abisoye', 'abimbola13@gmail.com', 'abimbola13')
        self.course = Course("BUS101", "Magic School Bus Rides")


    def test_view_enrolled_courses(self):
        self.student1.enroll_course(self.course)
        enrolled_courses = self.student1.view_enrolled_courses()
        self.assertEqual(len(enrolled_courses), 1)

    def test_login_success(self):
        self.assertTrue(self.student1.login('Abariwonda4@gmail.com', 'hamid123'))

    def test_login_fail_email(self):
        self.assertFalse(self.student1.login('wrong@example.com', 'hamid123'))

    def test_login_fail_password(self):
        self.assertFalse(self.student1.login('Abariwonda4@gmail.com', 'wrongPassword'))

    def test_enroll_multiple_courses(self):
        course2 = Course("ART101", "Drawing")
        self.student1.enroll_course(self.course)
        self.student1.enroll_course(course2)
        self.assertEqual(len(self.student1.courses), 2)

    def test_view_empty_enrolled_courses(self):
        enrolled_courses = self.student3.view_enrolled_courses()
        self.assertEqual(len(enrolled_courses), 0)

    def test_enroll_same_course_twice(self):
        self.student2.enroll_course(self.course)
        self.student2.enroll_course(self.course)
        self.assertEqual(len(self.student2.courses), 1)

    def test_view_enrolled_courses_after_removing(self):
        self.student1.enroll_course(self.course)
        self.course.remove_student(self.student1)
        enrolled_courses = self.student1.view_enrolled_courses()
        self.assertEqual(len(enrolled_courses), 0)

    def test_login_not_registered(self):
        student4 = Student('Tim', 'Jones', 'tim@example.com', 'newStudent')
        self.assertFalse(student4.login('tim@example.com', 'newStudent'))

    def test_student_invalid_email(self):
        with self.assertRaises(InvalidEmailPatternException):
            Student("Test", "User", "invalid_email", "password123")

    def test_student_invalid_password(self):
        with self.assertRaises(InvalidPasswordLengthException):
            Student("Test", "User", "test@example.com", "short")