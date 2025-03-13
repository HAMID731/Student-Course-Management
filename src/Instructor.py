from src.User import User
from src.validator import Validator
class Instructor(User):

    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)
        self.list_of_instructors = []
        self.courses = []
        self.is_logged_in = False

    def register(self, first_name, last_name, email, password):
        validator.validate_first_name(first_name)
        validator.validate_last_name(last_name)
        validator.validate_email(email)
        validator.validate_password(password)

        if email in Student.student_emails:
            raise ValueError("This email is already used by a student.")

        if email in Instructor.instructor_emails:
            raise ValueError("Email already in use by another instructor.")

        Instructor.instructor_emails.append(email)

        self.list_of_instructors.append({
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password
        })
        self.save_to_file(first_name, last_name, email, password)

        return True

    @staticmethod
    def save_to_file(first_name, last_name, email, password):
        try:
            with open("instructors.txt", "a") as file:
                file.write(f"First Name: {first_name}, Last Name: {last_name}, Email: {email}, Password: {password}\n")
        except Exception as e:
            print(f"Error saving instructor data: {e}")

    def login(self, email, password):
        validator.validate_email(email)
        validator.validate_password(password)

        for instructor in self.list_of_instructors:
            if instructor['email'] == email and instructor['password'] == password:
                self.is_logged_in = True
                return True
        raise VerificationFailedException("Invalid email or password")

    def add_course(self, course):
        self.courses.append(course)

    def view_enrolled_students(self, course_code):
        for course in self.courses:
            if course.course_code == course_code:
                print(f"Students in {course.course_title}:")
                for student in course.enrollment_students:
                    print(f"  - {student}")
                return
        print("Course not found for this instructor.")