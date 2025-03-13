from validator import Validator
from exceptions.exception import *
import os

from src.User import User
class Student(User):

    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)
        self.is_logged_in = False
        self.registered_users = {}
        self.enrolled_courses = {}
        self.list_of_students = []

    def register(self, first_name: str,last_name: str, email: str, password: str) -> bool:
        Validator.validate_first_name(first_name)
        Validator.validate_last_name(last_name)
        Validator.validate_email(email)
        Validator.validate_password(password)
        if email in Validator.email_exists:
            raise EmailAlreadyExistException("This email is already registered")
        self.list_of_students.append(Student(first_name, last_name, email, password))

    def login(self, email: str, password: str) -> bool:
        for  users in self.registered_users:
            if email in self.registered_users and password in self.registered_users:
                stored_email, stored_password = self.registered_users[email]
                if stored_password == password and stored_email == email:
                    self.is_logged_in = True
                    return True
            return False

    def find_course_by_name(self, course_name: str):
        for course in self.enrolled_courses:
            if course_name == course_name:
                return course
        raise ValueError(f"Course named {course_name} not found.")

    def find_course_by_code(self, course_code: str):
        pass
    def view_grades(self, grades):
        if self.enrolled_courses:
            for course in self.enrolled_courses:
                grade = grades.get(course, "No grade assigned")
                print(f"Grade for {course}: {grade}")
        else:
            print("No courses enrolled.")

    def view_course_info(self, course):
        print(f"Information about the course {course}: Course details here.")

    def enroll_course(self, param):
        pass

    def view_enrolled_courses(self, enrolled_courses):
        return len(self.enrolled_courses.get([]))
        print(f"Courses enrolled by {self.first_name} {self.last_name}:{', '.join(self.enrolled_courses)}")

def save_files(first_name,last_name,email):
    if not os.path.exists("student_files.txt"):
        return False
    with open("student_files.txt", "a") as file:
        file.write(f"{first_name} {last_name}:{email}\n")
def load_files(first_name,last_name,email):
    with open("student_files.txt", "r") as file:
        file.readline(f"{first_name} {last_name}:{email}\n")






















