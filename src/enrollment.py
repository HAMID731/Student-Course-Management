class Enrollment:

    def __init__(self, course, student):
        self.course = course
        self.student = student

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        self.__course = value

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        self.__student = value