import sys

from exceptions.exception import *
from src.course import Course


class Main:

    def main_menu(self):
        self.welcome()
        print("""
                   1 --> Register
                   2 --> Login
                   3 --> Exit
        """)

        print("Kindly enter any choice from the above:")
        choice = input("still waiting: ")

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
        print("""
                        1 --> Register as a teacher
                        2 --> Register as a student
                        3 --> Exit
                    """)
        choice = input("Kindly enter any choice from the above: ")
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
        print("Exiting App.")
        print(">>>>>>>>>>>>>>>>>>>>.")
        sys.exit(0)

    @staticmethod
    def welcome() -> None:
        print("Welcome\n")
        print("The next page Displays And Help You With Your Choice ?\n")

    def register_teacher(self):
        try:
            name = input("Enter your name(First and Last name): ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            instructor = Instructor(name, email, password)
            instructor.register(name, email, password)
            print(f"Dear {name}, You have successfully registered")
        except InvalidNameLengthException as e:
            print(f"Error {e}")
        except InvalidNameException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")
        finally:
            self.main_menu()

    def register_student(self):
        try:
            first_name = input("Enter your First name: ")
            last_name = input("Enter your Last name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            student = Student(name, email, password)
            student.register(name, email, password)
            print(f"Dear {name}, You have successfully registered")
        except InvalidNameLengthException as e:
            print(f"Error {e}")
        except InvalidNameException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")
        finally:
            self.main_menu()

    def login_menu(self):
        print("""
                                1 --> Login as a teacher
                                2 --> Login as a student
                                3 --> Exit
                            """)
        choice = input("Kindly enter any choice from the above: ")
        if choice == "1":
            self.login_teacher()
        elif choice == "2":
            self.login_student(student)
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
        except InvalidNameLengthException as e:
            print(f"Error {e}")
        except InvalidNameException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")
        finally:
            self.main_menu()

    def login_student(self, student):
        try:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            student.find_student(email)
            check = student.login(email, password)
            print("You have successfully logged in.")
        except InvalidNameLengthException as e:
            print(f"Error {e}")
        except InvalidNameException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")
        finally:
            self.main_menu()

    def login_teacher(self):
        try:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            instructor = Instructor.find_teacher(email)
            if instructor and instructor.login(email, password):
                print("\nYou have successfully logged in as Teacher.")
        except InvalidNameLengthException as e:
            print(f"Error: {e}")
        finally:
            self.teacher_menu()

    def teacher_menu(self, instructor: Instructor):
        try:
            print("""
            1 -> Add course
            2 -> View number of students registered
            3 -> Grade student
            4 -> logout
             """)
            choice = input("Kindly enter any choice from the above: ")

            if choice == "1":
                self.create_course(instructor)
            elif choice == '2':
                self.view_number_of_student_registered(instructor)
            elif choice == '3':
                self.grade_student(instructor)
            elif choice == '4':
                print("logging out mf...")
                self.main_menu()

        except InvalidNameLengthException as e:
                print(f"Error: {e}")

    def create_course(self, instructor):
        try:
            course_code = input("Enter course code: ")
            course_title = input("Enter course title: ")
            course = Course(course_code, course_title)
            instructor.create_course(course)
            print(f"You have created {course_code} successfully.")
        except InvalidCourseCodeException as e:
            print(f"Error {e}")
        except InvalidCourseTitleException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")
        finally:
            self.teacher_menu(instructor)

    def view_number_of_student_registered(self, instructor):
        try:
            course_code = input("Enter course code: ")
            instructor.view_enrolled_students(course_code)
        except InvalidCourseCodeException as e:
            print(f"Error {e}")
        finally:
            self.login_teacher()

    def grade_student(self, instructor):
        try:
            student_name = input("Enter student name: ")
            first_ca = input("Enter student first ca: ")
            second_ca = input("Enter student second ca: ")
            exam = input("Enter student exam score: ")
            instructor.grade_student(student_name, first_ca, second_ca, exam)
        except InvalidNameLengthException as e:
            print(f"Error {e}")
        except InvalidNameException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")
        finally:
            self.login_teacher()


    def student_menu(self, student):
        print("""
            1. View Courses
            2. Enroll Course(s)
            3. View grades
            4. Logout
            """)
        choice = input("Kindly enter any choice from the above: ")

        if choice == "1":
            student.view_courses()
        elif choice == "2":
            student.view_enrolled_courses()
        elif choice == "3":
            self.view_grade(student)
        elif choice == "4":
            self.main_menu()
        else:
            self.main_menu()

    def view_grade(self, student):
        try:
            course_code = input("Enter course code: ")
            print(f"Your grades for {course_code} are: ")
            student.view_grades(course_code)



if __name__ == "__main__":
    app = Main()
    app.main_menu()


# points: exceptions in instructors class
# self.login exception
# grade student method is missing

