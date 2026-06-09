from app.db.db_connection import get_cur

def get_user(user_id):
    with get_cur() as cur:
        cur.execute("SELECT username, role from users where user_id = %s", (user_id,))
        user = cur.fetchone()
        
    return user