import os
import re

from exceptions.exception import *


class Validator:

   @staticmethod
   def validate_first_name(first_name) -> bool:
       if not first_name:
           raise NullException("First Name field is required")
       if not first_name.strip(" "):
           raise InvalidNameLengthException("No spaces allowed amongst the letters.")
       if len(first_name) < 3 or not first_name.isalpha():
           raise InvalidNameLengthException("Last Name must be at least 3 characters long and contain only letters.")
       return True

   @staticmethod
   def validate_last_name(last_name: str) -> bool:
       if not last_name:
           raise NullException("Last Name field is required")
       if not last_name.strip(" "):
           raise InvalidNameLengthException("No spaces allowed amongst the letters.")
       if len(last_name) < 3 or not last_name.isalpha():
           raise InvalidNameLengthException("Last Name must be at least 3 characters long and contain only letters.")
       return True

   @staticmethod
   def validate_email(email_input: str) -> bool:
       if not email_input:
           raise NullException("Email field is required")

       if not isinstance(email_input, str):
           raise InvalidEmailPatternException("Email must be a string")

       if not email_input.strip(" "):
           raise InvalidEmailPatternException("Email should not be spaced")

       email_pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.(com|africa|org|ng|yahoo)$'

       if email_pattern.endswith(".") or email_pattern.startswith("."):
           raise InvalidEmailPatternException("Email should not end with a period")

       if not re.match(email_pattern, email_input):
           raise InvalidEmailPatternException("Invalid email address.")

       return True

   @staticmethod
   def validate_password(password: str) -> bool:
       if not password:
           raise NullException("Password field is required")
       if not password.strip(" "):
           raise InvalidPasswordLengthException("Invalid.")
       if len(password) < 5:
           raise InvalidPasswordLengthException("Password must be at least 5 characters long and contain only letters.")
       return True

   @staticmethod
   def validate_course_code(course_code: str) -> bool:
       if not course_code:
           raise NullException("Course Code field is required")
       if len(course_code) < 5 or len(course_code) > 7 or not course_code.strip(" "):
           raise InvalidCourseCodeException("Course Code should not be spaced.")
       if not course_code.isalnum():
           raise InvalidCourseCodeException("Course Code should both be alphabets and numbers.")
       return True

   @staticmethod
   def validate_course_title(course_title: str) -> bool:
       if not course_title:
           raise NullException("Course Title field is required")
       if len(course_title) < 3:
           raise InvalidCourseTitleException("Course Title should not be spaced.")
       return True


   @staticmethod
   def register_email(email):
        if not os.path.exists("email.txt"):
            raise InvalidEmailPatternException("Email file does not exist.")
        try:
            with open("email.txt", 'a') as file:
               file.write(email)
        except FileNotFoundError as e:
            return e

   @staticmethod
   def email_exists(email: str):
       try:
           with open("email.txt", 'r') as file:
               file.read(email)
       except FileExistsError:
           return False








