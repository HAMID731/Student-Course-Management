from exceptions.exception import InvalidNameLengthException, AlreadyExistException
from src.validator import Validator


class Course:

    def __init__(self, course_code, course_title):
        Validator.validate_course_code(course_code)
        Validator.validate_course_title(course_title)
        self.course_code = course_code
        self.course_title = course_title
        self.courses = []
        self.enrollment_students = []

    @property
    def course_code(self):
        return self.__course_code

    @course_code.setter
    def course_code(self, course_code):
        self.__course_code = course_code

    @property
    def course_title(self):
        return self.__title

    @course_title.setter
    def course_title(self, course_title):
        self.__title = course_title


    def add_student(self, student_name: str):
        try:
            first_name, last_name = student_name.split()
        except ValueError:
            raise InvalidNameLengthException("Invalid student name format.")

        if student_name in self.enrollment_students:
            raise AlreadyExistException("Student already exists")

        self.enrollment_students.append(student_name)

    def remove_student(self, student_name: str) -> bool:
        try:
            first_name, last_name = student_name.split()
            self.enrollment_students.remove(student_name)
            return True
        except InvalidNameLengthException:
            print("Invalid student name format.")

    def get_number_of_enrolled_students(self):
        return len(self.enrollment_students)

