import os
from exceptions.exception import *
from .student import Student
from .validator import Validator
from src.User import User
from src.password_encrypt import PasswordEncrypt
from .course import Course

class Instructor(User):
    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)
        self.courses = []
        self.is_logged_in = False

    def get_number_of_courses_created(self):
        return len(self.courses)

    def register(self, first_name: str,last_name: str, email: str, password: str):
        try:
            with open("courses.txt", 'a') as file:
                details = file.write(f'{first_name},{last_name},{email},{PasswordEncrypt.hash_password(password)}\n')
                # self.courses.append(details)
        except FileNotFoundError:
            print("File not found")



        # Validator.validate_first_name(first_name)
        # Validator.validate_last_name(last_name)
        # Validator.validate_email(email)
        # Validator.validate_password(password)
        # if email in Validator.email_exists:
        #     raise EmailAlreadyExistException("This email is already registered")
        # return True





    def login(self, email, password):
        if self.email == email and self.check_password(password):
            self.is_logged_in = True
            return True
        return False

    def create_course(self, course_code, course_title):
        new_course = Course(course_code, course_title)
        self.courses.append(new_course)
        return new_course

    def view_enrolled_students(self, course):
        return course.enrolled_students

    def number_of_enrolled_students(self, course):
        return len(course.enrolled_students)

    def assign_grade(self, student, first_ca, second_ca, exam):
        print(f"Assigning grades to {student.first_name}: CA1={first_ca}, CA2={second_ca}, Exam={exam}")
        return True

    def remove_student_from_course(self, student, course):
        if course in self.courses and student in course.enrolled_students:
            course.remove_student(student)
            return True
        return False

def save_to_file(instructors, fileName='instructors.txt'):
        # hashed_password = PasswordEncrypt.hash_password(self.password)
    if not os.path.exists(fileName):
        raise FileNotFoundError("file does not exist.")
    with open("instructors.txt", "w") as file:
        for instructor in instructors:
            file.write(f"{instructor.first_name},{instructor.last_name},{instructor.email},{PasswordEncrypt.hash_password(instructor.password)}\n")


def load_from_file():
    instructors = []
    if os.path.exists("instructors.txt"):
        with open("instructors.txt", "r") as file:
            for line in file:
                first_name, last_name, email, hashed_password = line.strip().split(",")
                instructor = Instructor(first_name, last_name, email, hashed_password)
                # instructor.__password = hashed_password
                instructors.append(instructor)
            return instructors