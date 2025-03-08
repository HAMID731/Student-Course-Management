from src.User import User


class Instructor(User):
    def __init__(self, email, password, instructor_id):
        super().__init__(email, password)
        self.instructor_id = instructor_id

    def display_info(self):
        print(f"Instructor ID: {self.instructor_id}, Email: {self.email}")