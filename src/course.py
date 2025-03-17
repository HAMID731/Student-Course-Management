import os
from exceptions.exception import *
from src.validator import Validator

class Course:
    def __init__(self, course_code, course_title):
        if not Validator.validate_course_code(course_code):
            raise InvalidCourseCodeException("Invalid course code format.")
        if not Validator.validate_course_title(course_title):
            raise InvalidCourseTitleException("Invalid course title format.")
        self.course_code = course_code
        self.course_title = course_title
        self.enrolled_students = []

    def add_student(self, student):
        self.enrolled_students.append(student)

    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)

    def number_of_enrolled_students(self):
        return len(self.enrolled_students)

    def save_to_file(self):
        with open("courses.txt", "a") as file:
            file.write(f"{self.course_code},{self.course_title}\n")

    @staticmethod
    def load_from_file():
        courses = []
        if os.path.exists("courses.txt"):
            with open("courses.txt", "r") as file:
                for line in file:
                    course_code, course_title = line.strip().split(",")
                    course = Course(course_code, course_title)
                    courses.append(course)
        return courses