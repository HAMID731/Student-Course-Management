import sys
from exceptions.exception import *
from src.student import Student
from src.Instructor import Instructor
from src.course import Course

class Main:

    def __init__(self):
        self.logged_in_instructor = None
        self.logged_in_student = None

    def display_menu(self, menu_options, prompt):
        """Displays a menu and gets user input."""
        print(menu_options)
        return input(prompt)

    def main_menu(self):
        self.welcome()
        choice = self.display_menu(
            """
            1 --> Register
            2 --> Login
            3 --> Exit
            """,
            "Kindly enter your choice: "
        )

        match choice:
            case "1":
                self.register_menu()
            case "2":
                self.login_menu()
            case "3":
                self.exit_app()
            case _:
                self.main_menu()

    def register_menu(self):
        choice = self.display_menu(
            """
            1 --> Register as a teacher
            2 --> Register as a student
            3 --> Exit
            """,
            "Kindly enter your choice: "
        )

        if choice == "1":
            self.register_teacher()
        elif choice == "2":
            self.register_student()
        elif choice == "3":
            self.exit_app()
        else:
            self.main_menu()

    @staticmethod
    def exit_app():
        print("Exiting App.\n>>>>>>>>>>>>>>>>>>>>.")
        sys.exit(0)

    @staticmethod
    def welcome():
        print("Welcome\nThe next page displays and helps you with your choice.\n")

    def register_teacher(self):
        try:
            first_name = input("Enter your First name: ")
            last_name = input("Enter your Last name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            instructor = Instructor(first_name, last_name, email, password)
            instructor.register(first_name, last_name, email, password)
            print(f"Dear {first_name}, you have successfully registered.")
        except (InvalidNameLengthException, InvalidNameException, NullException, EmailAlreadyExistException) as e:
            print(f"Error: {e}")
        finally:
            self.main_menu()

    def register_student(self):
        try:
            first_name = input("Enter your First name: ")
            last_name = input("Enter your Last name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            student = Student(first_name, last_name, email, password)
            student.register(first_name, last_name, email, password)
            print(f"Dear {first_name}, you have successfully registered.")
        except (InvalidNameLengthException, InvalidNameException, NullException, EmailAlreadyExistException) as e:
            print(f"Error: {e}")
        finally:
            self.main_menu()

    def login_menu(self):
        choice = self.display_menu(
            """
            1 --> Login as a teacher
            2 --> Login as a student
            3 --> Exit
            """,
            "Kindly enter your choice: "
        )

        if choice == "1":
            self.login_teacher()
        elif choice == "2":
            self.login_student()
        elif choice == "3":
            self.exit_app()
        else:
            self.main_menu()

    def login_teacher(self):
        try:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            instructor = Instructor.find_teacher(email)
            if instructor and instructor.login(email, password):
                print("\nYou have successfully logged in as Teacher.")
                self.logged_in_instructor = instructor
                self.teacher_menu(self.logged_in_instructor)
            else:
                print("Invalid login credentials.")
        except (InvalidNameLengthException, InvalidNameException, NullException, VerificationFailedException) as e:
            print(f"Error: {e}")
        finally:
            if not self.logged_in_instructor:
                self.main_menu()

    def login_student(self):
        try:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            student = Student.find_student(email)
            if student and student.login(email, password):
                print("You have successfully logged in.")
                self.logged_in_student = student
                self.student_menu(self.logged_in_student)
            else:
                print("Invalid login credentials.")
        except (InvalidNameLengthException, InvalidNameException, NullException, VerificationFailedException) as e:
            print(f"Error: {e}")
        finally:
            if not self.logged_in_student:
                self.main_menu()

    def teacher_menu(self, instructor):
        while self.logged_in_instructor:
            choice = self.display_menu(
                """
                1 -> Add course
                2 -> View number of students registered
                3 -> Grade student
                4 -> Logout
                """,
                "Kindly enter your choice: "
            )

            try:
                if choice == "1":
                    self.create_course(instructor)
                elif choice == "2":
                    self.view_number_of_student_registered(instructor)
                elif choice == "3":
                    self.grade_student(instructor)
                elif choice == "4":
                    print("Logging out...")
                    self.logged_in_instructor = None
                else:
                    print("Invalid choice.")
            except (InvalidNameLengthException, InvalidCourseCodeException, InvalidCourseTitleException, NullException, InvalidNameException, ValueError) as e:
                print(f"Error: {e}")

            if not self.logged_in_instructor:
                self.main_menu()

    def create_course(self, instructor):
        try:
            course_code = input("Enter course code: ")
            course_title = input("Enter course title: ")
            course = Course(course_code, course_title)
            instructor.add_course(course)
            print(f"You have created {course_code} successfully.")
        except (InvalidCourseCodeException, InvalidCourseTitleException, NullException) as e:
            print(f"Error: {e}")

    def view_number_of_student_registered(self, instructor):
        try:
            course_code = input("Enter course code: ")
            instructor.view_enrolled_students(course_code)
        except InvalidCourseCodeException as e:
            print(f"Error: {e}")

    def grade_student(self, instructor):
        try:
            student_name = input("Enter student name: ")
            first_ca = int(input("Enter student first ca: "))
            second_ca = int(input("Enter student second ca: "))
            exam = int(input("Enter student exam score: "))
            instructor.grade_student(student_name, first_ca, second_ca, exam)
        except (InvalidNameLengthException, InvalidNameException, NullException, ValueError) as e:
            print(f"Error: {e}")

    def student_menu(self, student):
        while self.logged_in_student:
            choice = self.display_menu(
                """
                1. View Courses
                2. Enroll Course(s)
                3. View grades
                4. Logout
                """,
                "Kindly enter your choice: "
            )

            try:
                if choice == "1":
                    student.view_courses()
                elif choice == "2":
                    student.view_enrolled_courses()
                elif choice == "3":
                    self. view_grade(student)
                elif choice == "4":
                    print("Logging out...")
                    self.logged_in_student = None
                else:
                    print("Invalid choice.")
            except Exception as e:
                print(f"Error: {e}")

            if not self.logged_in_student:
                self.main_menu()
