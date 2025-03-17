import os
from src.User import User
from src.password_encrypt import PasswordEncrypt
from course import Course

class Instructor(User):
    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)
        self.courses = []
        self.is_logged_in = False

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

    def save_to_file(self):
        hashed_password = PasswordEncrypt.hash_password(self.password)
        with open("instructors.txt", "a") as file:
            file.write(f"{self.first_name},{self.last_name},{self.email},{hashed_password.decode()}\n")

    @staticmethod
    def load_from_file():
        instructors = []
        if os.path.exists("instructors.txt"):
            with open("instructors.txt", "r") as file:
                for line in file:
                    first_name, last_name, email, hashed_password = line.strip().split(",")
                    instructor = Instructor(first_name, last_name, email, "dummy_password")
                    instructor.__password = hashed_password
                    instructors.append(instructor)
        return instructors