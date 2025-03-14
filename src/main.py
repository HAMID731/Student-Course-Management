import sys

from exceptions.exception import *

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
            teacher = Instructor(name, email, password)
            teacher.register(name, email, password)
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
            name = input("Enter your name(First and Last name): ")
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
            self.login_student()
        elif choice == "3":
            self.exit_app()
        else:
            self.main_menu()

    def login_teacher(self):
        try:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            student = Student(email, password)
            teacher.find_teacher(email)
            teacher.login(email, password)
            print("You have successfully logged in.")
        except InvalidNameLengthException as e:
            print(f"Error {e}")
        except InvalidNameException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")
        finally:
            self.main_menu()

    def login_student(self):
        try:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            student = Student(email, password)
            student.find_student(email)
            check = teacher.login(email, password)
            if check:
                print("You have successfully logged in.")
            print("""
                1. View Courses
                2. Enroll Course(s)
                3. Logout 
                """)
            choice = input("Kindly enter any choice from the above: ")

            if choice == "1":
                student.view_courses()
            elif choice == "2":
                student.view_enrolled_courses()
            elif choice == "3":
                self.main_menu()
            else:
                self.main_menu()

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

            self.teacher.find_teacher(email)
            check = self.teacher.login(email, password)
            if check:
                print("You have successfully logged in.")

            print("""
            1 -> Add course
            2 -> View number of students registered
            3 -> Grade student
            4 -> logout
             """)
            choice = input("Kindly enter any choice from the above: ")

            if choice == "1":
                self.create_course(email)
            elif choice == '2'
                self.view_number_of_student_registered
            elif choice == '3':
                self.grade_student
            elif choice == '4':
                print("logging out mf...")
                self.main_menu()

        except InvalidNameLengthException as e:
            print(f"Error: {e}")

    def create_course(self,email):
        try:
            course_code = input("Enter course code: ")
            course_title = input("Enter course title: ")
            teacher =
            course = Course(course_code, course_title)
            # teacher = Teacher()
            self.teacher.create_course(course_code, course_title)
        except InvalidCourseCodeException as e:
            print(f"Error {e}")
        except InvalidCourseTitleException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")
        finally:
            self.main_menu()

if __name__ == "__main__":
    app = Main()
    app.main_menu()


