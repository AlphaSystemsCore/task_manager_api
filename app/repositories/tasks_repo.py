from app.db.db_connection import get_cur
def create_task_repo(name:str, category, user_id, status, time_to_be_completed):
    with get_cur() as cur:
        cur.execute("INSERT INTO tasks(name, category, user_id, status, time_to_completed) VALUES(%s, %s, %s, %s, %s)",
         (name, category, user_id, status, time_to_completed))
        

if __name__ == "__main__":
    create_task_repo("coding", "school",  )