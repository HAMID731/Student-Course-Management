from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,first_name,last_name,email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

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
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password