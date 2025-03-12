import unittest
from src.Instructor import Instructor
from src.User import User
from src.validator import Validator
from exceptions.exception import VerificationFailedException
from src.Student import Student
import os

class TestInstructor(unittest.TestCase):

    def setUp(self):
        self.instructor = Instructor("Test", "Instructor", "test@instructor.com", "password123")
        self.student = Student("Test", "Student", "test@student.com", "password123")
        Instructor.instructor_emails = []
        Student.student_emails = []
        Instructor.list_of_instructors = []
        if os.path.exists("instructors.txt"):
            os.remove("instructors.txt")

    def test_register_success(self):
        self.assertTrue(self.instructor.register("John", "Doe", "john@example.com", "securepass"))
        self.assertEqual(len(Instructor.list_of_instructors), 1)

    def test_register_duplicate_email(self):
        self.instructor.register("John", "Doe", "john@example.com", "securepass")
        with self.assertRaises(ValueError):
            self.instructor.register("Jane", "Doe", "john@example.com", "anotherpass")

    def test_register_student_email_conflict(self):
        self.student.register("Student", "One", "student@example.com", "studentpass")
        with self.assertRaises(ValueError):
            self.instructor.register("Instructor", "One", "student@example.com", "instructorpass")

    def test_login_success(self):
        self.instructor.register("John", "Doe", "john@example.com", "securepass")
        self.assertTrue(self.instructor.login("john@example.com", "securepass"))

    def test_login_failure_email(self):
        self.instructor.register("John", "Doe", "john@example.com", "securepass")
        with self.assertRaises(VerificationFailedException):
            self.instructor.login("wrong@example.com", "securepass")

    def test_login_failure_password(self):
        self.instructor.register("John", "Doe", "john@example.com", "securepass")
        with self.assertRaises(VerificationFailedException):
            self.instructor.login("john@example.com", "wrongpass")

    def test_add_course(self):
        course = Course("CS101", "Intro to CS")
        self.instructor.add_course(course)
        self.assertEqual(len(self.instructor.courses), 1)

    def test_view_enrolled_students(self):
        course = Course("CS101", "Intro to CS")
        student1 = Student("Alice")
        student2 = Student("Bob")
        course.enrollment_students.append(student1)
        course.enrollment_students.append(student2)
        self.instructor.add_course(course)
        self.instructor.view_enrolled_students("CS101")

if __name__ == '__main__':
    unittest.main()