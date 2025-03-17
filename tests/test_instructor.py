import unittest
from src.Instructor import Instructor
from src.student import Student
from src.course import Course
from exceptions.exception import InvalidCourseCodeException, InvalidCourseTitleException

class TestInstructor(unittest.TestCase):

    def setUp(self):
        self.instructor = Instructor("chibuzor", "sikiru", "friz@example.com", "magicSchoolBus")
        self.student1 = Student('Abari', 'Hamid', 'Abariwonda4@gmail.com', 'hamid123')
        self.student2 = Student('favour', 'igwe', 'favor123@gmail.com', 'favour123')
        self.student3 = Student('abimbola', 'abisoye', 'abimbola13@gmail.com', 'abimbola13')
        self.course = Course("BUS101", "Magic School Bus Rides")

    def test_instructor_can_be_registered(self):
        first_instructor = self.instructor.register("chibuzor", "sikiru", "friz@example.com","pass")

    def test_instructor_can_create_course(self):
        self.instructor.create_course("SCI101", "All About Science")
        self.assertEqual(self.instructor.get_number_of_courses_created(), 1)
        self.instructor.create_course("ART101","Intro")
        self.assertEqual(self.instructor.get_number_of_courses_created(), 2)
        self.instructor.create_course("ART201", "Intro2")
        self.assertEqual(self.instructor.get_number_of_courses_created(), 3)

    def test_assign_grade(self):
        result = self.instructor.assign_grade(self.student1, 90, 85, 95)
        self.assertTrue(result)
    #
    # def test_login_success(self):
    #     self.assertTrue(self.instructor.login("frizzle@example.com", "magicSchoolBus"))
    #
    # def test_login_fail_email(self):
    #     self.assertFalse(self.instructor.login("wrong@example.com", "magicSchoolBus"))
    #
    # def test_login_fail_password(self):
    #     self.assertFalse(self.instructor.login("frizzle@example.com", "wrongPassword"))
    #
    # def test_view_enrolled_students(self):
    #     self.course.add_student(self.student1)
    #     enrolled_students = self.instructor.view_enrolled_students(self.course)
    #     self.assertEqual(len(enrolled_students), 1)
    #
    # def test_number_of_enrolled_students(self):
    #     self.course.add_student(self.student2)
    #     self.assertEqual(self.instructor.number_of_enrolled_students(self.course), 1)
    #
    # def test_remove_nonexistent_student(self):
    #     result = self.instructor.remove_student_from_course(self.student3, self.course)
    #     self.assertFalse(result)
    #
    # def test_remove_student_from_nonexistent_course(self):
    #     new_course = Course("ART101", "Drawing")
    #     result = self.instructor.remove_student_from_course(self.student1, new_course)
    #     self.assertFalse(result)
    #
    # def test_create_course_invalid_code(self):
    #     with self.assertRaises(InvalidCourseCodeException):
    #         self.instructor.create_course("INVLD", "Invalid Code Course")
    #
    # def test_create_course_invalid_title(self):
    #     with self.assertRaises(InvalidCourseTitleException):
    #         self.instructor.create_course("ART101", "Art")