from app.auth.password_handler import hash_password
from app.repositories.auth_repo import get_email,save_credentials
from app.core.exeptions import EmailAlreadyExistsError
from psycopg2.errors import UniqueViolation


def register_user_service(email, password):
    #register user by credentials
    hashed_password = hash_password(password)
    try:
        save_credentials(email, hashed_password)
        return {"message": "User register successfully"}
    except UniqueViolation as e:
        raise EmailAlreadyExistsError()
    








# for testing and debugging
if  __name__ == "__main__":
    register_user_service('alpa@get_email', 'asdfaadf')