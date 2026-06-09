from app.repositories.user_repo import get_user

def get_user_service(user_id):
    user = get_user(user_id)
    if user is None:
        return None
    return user
