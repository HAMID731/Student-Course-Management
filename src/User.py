from src.password_encrypt import *
from abc import ABC, abstractmethod
from src.validator import Validator

class User(ABC):
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password(password)

    @abstractmethod
    def register(self, first_name, last_name, email, password):
        pass

    @abstractmethod
    def login(self, email, password):
        pass

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = Validator.validate_first_name(first_name)

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = Validator.validate_last_name(last_name)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = Validator.validate_email(email)

    def set_password(self, password):
        hashed_password = PasswordEncrypt.hash_password(password)
        self.__password = hashed_password

    def check_password(self, password):
        return PasswordEncrypt.check_password(password, self.__password)

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed directly.")