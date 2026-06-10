from app.db.db_connection import get_cur

def create_task_repo(name:str, category:str, user_id:str, duration:str):
    with get_cur() as cur:
        cur.execute("INSERT INTO tasks(name, category, user_id, time_to_be_completed) VALUES(%s, %s, %s, %s) RETURNING task_id",
        (name, category, user_id, duration))
        task_id = cur.fetchone()
    return task_id

def get_tasks_repo(user_id:str, limit: int, offset:int):
    with get_cur() as cur:
        cur.execute("SELECT name, category, status, time_created, time_to_be_completed, time_completed FROM tasks WHERE user_id = %s LIMIT %s OFFSET %s", (user_id, limit, offset))
        rows = cur.fetchall()
    return rows


