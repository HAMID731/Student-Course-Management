import os

from src.course import Course


class Enrollment:

    def __init__(self, course: Course, student):
        self.course = course
        self.student = student

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        self.__course = value

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        self.__student = value

    def __repr__(self):
        return f'{self.course} {self.student}'

    @staticmethod
    def save_enrollment(course, student):
        if not os.path.exists('enrollment.txt'):
            with open('enrollment.txt', 'w') as file:
                file.write(f'{course}, {student}')

    @staticmethod
    def load_enrollment():
        if os.path.exists('enrollment.txt'):
            with open('enrollment.txt', 'r') as file:
                file.readline()