from src.User import User

class Instructor(User):
    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)
        self.list_of_instructors = []
        self.courses = []
        self.is_logged_in = False

    def create_course(self, course_code, course_title):
        Validator.validate_course_code(course_code)
        Validator.validate_course_title(course_title)
        new_course = Course(course_code, course_title)
        self.courses.append(new_course)
        return new_course

    def register(self, first_name, last_name, email, password):
        Validator.validate_first_name(first_name)
        Validator.validate_last_name(last_name)
        validator.validate_email(email)
        Validator.validate_password(password)


    def login(self, email, password):


    def assign_grade(self, course_code, student_id, first_ca, second_ca, exam):
        pass

    def view_enrolled_students_course(self, course):
        return course.enrolled_students

    def number_of_enrolled_students_course(self, course):
        return len(course.enrolled_students)