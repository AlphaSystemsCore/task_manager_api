from app.auth.password_handler import hash_password, verify_password, DUMMY_HASH
from app.repositories.auth_repo import get_email,save_credentials, get_hash_password, get_user_id
from app.core.exeptions import EmailAlreadyExistsError,  EmailDoesNotExistsError, CredentialsError
from psycopg2.errors import UniqueViolation


def register_user_service(email:str, password:str):
    #register user by credentials
    hashed_password = hash_password(password)
    try:
        save_credentials(email, hashed_password)
        return {"message": "User register successfully"}
    except UniqueViolation:
        raise EmailAlreadyExistsError()
    
def authenticate_user(email, password):
    email = get_email(email)
    if email is None:
        verify_password(password, DUMMY_HASH)
        raise CredentialsError
    hashed_password = get_hash_password(email)[0]
    if verify_password(password, hashed_password):
        user_id = get_user_id(email)
        return user_id
    raise CredentialsError

    







# for testing and debugging
if  __name__ == "__main__":
    register_user_service('alpa@get_email', 'asdfaadf')