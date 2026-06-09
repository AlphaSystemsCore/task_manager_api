from app.db.db_connection import get_cur

def save_credentials(email, hashed_password):
    #save user credentials  and populates user using credentials_id
    with get_cur() as cur:
        cur.execute("INSERT INTO credentials(email, hashed_password) VALUES(%s, %s)  RETURNING credential_id", (email, hashed_password))
        credential_id = cur.fetchone()
        cur.execute("INSERT INTO users (credential_id) VALUES(%s)", credential_id)

def get_hash_password(email):
    with get_cur() as cur:
        cur.execute("SELECT hashed_password FROM credentials WHERE email = %s ", (email,))
        hashed_password = cur.fetchone()
    return hashed_password

def get_user_id(email):
    # get user id used in log in after user logs in with email and password
    with get_cur() as cur:
        cur.execute(
            """
            SELECT user_id FROM users u
            LEFT JOIN credentials c
            ON u.credential_id = c.credential_id
            WHERE email = %s
            """, (email,)
        )
        user_id = cur.fetchone()
        return user_id

def get_email(email):
    with get_cur() as cur:
        cur.execute("SELECT email FROM credentials WHERE email = %s", (email,))
        email = cur.fetchone()
    return email



#for testing and debbuging
# if __name__ == "__main__":
#     # save_credentials(, "sjadfljalskfdj")
#     print(get_user_id("alpha@outlook.com"))
