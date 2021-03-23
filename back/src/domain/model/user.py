import hashlib


def hash_password(password):
    hash_obj = hashlib.md5(password.encode())
    return hash_obj.hexdigest()


class User:
    def __init__(
        self,
        user_id,
        username,
        password,
        user_mail,
        user_rol,
        user_status,
        user_surename,
        
    ):
        self.user_id = user_id
        self.username = username
        self.user_mail = user_mail
        self.user_rol = user_rol
        self.password = password
        self.user_status = user_status
        self.user_surename = user_surename

    def check_password(self, password):
        return hash_password(password) == self.password 
    
    def __getstate__(self):

        return {
            "user_id": self.user_id,
            "user_username": self.user_username,
            "user_mail": self.user_mail,
            "user_rol": self.user_rol,
            "user_status": self.user_status,
        }
