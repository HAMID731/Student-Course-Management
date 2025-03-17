import unittest
from src.Instructor import Instructor
from src.student import Student
from src.course import Course

class TestInstructor(unittest.TestCase):

    def setUp(self):
        self.instructor = Instructor("Ms.", "Frizzle", "frizzle@example.com", "magicSchoolBus")
        self.student1 = Student("Arnold", "Perlstein", "arnold@example.com", "iHateFieldTrips")
        self.student2 = Student("Carlos", "Ramon", "carlos@example.com", "whatAboutIt")
        self.course = Course("BUS101", "Magic School Bus Rides")

    def test_create_course(self):
        new_course = self.instructor.create_course("SCI101", "All About Science")
        self.assertIsNotNone(new_course)
        self.assertEqual(len(self.instructor.courses), 1)

    def test_add_remove_student(self):
        self.course.add_student(self.student1)
        self.assertEqual(len(self.course.enrolled_students), 1)
        self.instructor.remove_student_from_course(self.student1, self.course)
        self.assertEqual(len(self.course.enrolled_students), 0)

    def test_assign_grade(self):
        # Since assign_grade is a placeholder, we'll just check if it runs
        self.instructor.assign_grade(self.student1, 90, 85, 95)

    def test_login_success(self):
        self.assertTrue(self.instructor.login("frizzle@example.com", "magicSchoolBus"))
        self.assertTrue(self.instructor.is_logged_in)

    def test_login_fail_email(self):
        self.assertFalse(self.instructor.login("wrong@example.com", "magicSchoolBus"))
        self.assertFalse(self.instructor.is_logged_in)

    def test_login_fail_password(self):
        self.assertFalse(self.instructor.login("frizzle@example.com", "wrongPassword"))
        self.assertFalse(self.instructor.is_logged_in)

    def test_view_enrolled_students(self):
        self.course.add_student(self.student1)
        enrolled_students = self.instructor.view_enrolled_students(self.course)
        self.assertIn(self.student1, enrolled_students)

    def test_number_of_enrolled_students(self):
        self.course.add_student(self.student1)
        self.assertEqual(self.instructor.number_of_enrolled_students(self.course), 1)

    def test_remove_nonexistent_student(self):
        result = self.instructor.remove_student_from_course(self.student2, self.course)
        self.assertFalse(result)

    def test_remove_student_from_nonexistent_course(self):
        new_course = Course("ART101", "Drawing")
        result = self.instructor.remove_student_from_course(self.student1, new_course)
        self.assertFalse(result)