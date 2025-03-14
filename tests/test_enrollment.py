import unittest

from src.course import Course
from src.enrollment import Enrollment


class MyEnrollmentTestCase(unittest.TestCase):
    def test_that_course_can_be_gotten(self):
        name = "Favour"
        course = Course("Yor123", "yoruba language")
        enrollment = Enrollment(course, name)
        self.assertTrue(enrollment)
        self.assertEqual(course, enrollment.course)


    def test_that_student_can_be_enrolled(self):
        name = "Favour"
        course = Course("Yor123", "yoruba language")
        enrollment = Enrollment(course, name)
        self.assertTrue(enrollment)
        self.assertEqual(name, enrollment.student)