import bcrypt

class PasswordEncrypt:
    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password

    @staticmethod
    def check_password(password, hashed_password):
        return bcrypt.checkpw(password.encode(), hashed_password)