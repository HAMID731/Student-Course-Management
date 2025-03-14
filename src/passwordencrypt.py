import bcrypt

class PasswordEncrypt:


    def _init_(self, password: str):
        self.password = password

    def hash_password(self) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(self.password.encode(), salt)
        return hashed_password.decode()

    def save_to_file(self, file_name: str) :
        hashed_password = self.hash_password()
        with open(file_name, 'w') as file:
            file.write(hashed_password)
            print(f"Hashed password saved to {file_name}")