class Course:

    def __init__(self, course_code, course_title):
        self.course_code = course_code
        self.course_title = course_title
        self.courses = []

    @property
    def course_code(self):
        return self.__course_code

    @course_code.setter
    def course_code(self, course_code):
        self.__course_code = course_code

    @property
    def course_title(self):
        return self.__title

    @course_title.setter
    def course_title(self, course_title):
        self.__title = course_title


