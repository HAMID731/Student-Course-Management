from src.User import User

class Instructor(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.courses = []
        self.is_logged_in = False

    def create_course(self, course_code, course_title):
        new_course = Course(course_code, course_title)
        self.courses.append(new_course)
        return new_course

    def register(self, name, first_name, last_name, email, password):
        self.is_logged_in = True
        return True

    def login(self, email, password):
        self.is_logged_in = True
        return True

    def assign_grade(self, course_code, student_id, first_ca, second_ca, exam):
        pass

    def view_enrolled_students_course(self, course):
        return course.enrolled_students

    def number_of_enrolled_students_course(self, course):
        return len(course.enrolled_students)