from app.db.db_connection import get_cur
from datetime import datetime

def create_task_repo(name:str, category:str, user_id:str, duration:str):
    with get_cur() as cur:
        cur.execute("INSERT INTO tasks(name, category, user_id, time_to_be_completed) VALUES(%s, %s, %s, %s) RETURNING task_id",
        (name, category, user_id, duration))
        task_id = cur.fetchone()
    return task_id

def get_tasks_repo(user_id:str, limit: int, offset:int):
    with get_cur() as cur:
        cur.execute("SELECT task_id, name, category, status, time_created, time_to_be_completed, time_completed FROM tasks WHERE user_id = %s LIMIT %s OFFSET %s", (user_id, limit, offset))
        rows = cur.fetchall()
    return rows


def get_task_by_name_repo(user_id, task_name):
    with get_cur() as cur:
        cur.execute("""SELECT task_id, name, category, status, time_created, time_to_be_completed, time_completed 
        FROM tasks 
        WHERE user_id = %s AND name = %s""",
        (user_id, task_name))
        row = cur.fetchone()
    return row

def update_task_repo(
    user_id:str,
    task_id:str,
    name: str|None = None,
    category:str| None = None,
    time_to_be_completed: str| None = None
 ):
    with get_cur() as cur:
        cur.execute("""
            UPDATE tasks 
            SET
                name = COALESCE(%s, name),
                category = COALESCE(%s, category),
                time_to_be_completed =  COALESCE(%s,time_to_be_completed)
            WHERE task_id = %s AND user_id = %s
            """,
            (name, category, time_to_be_completed, task_id, user_id)
        )
        
def update_status_repo(user_id:str, task_id:str, status:str, time_completed:datetime | None ):
    with get_cur() as cur:
        cur.execute(
            """
            UPDATE tasks
            SET 
                status = %s,
                time_completed = COALESCE(%s, time_completed)
            WHERE task_id = %s AND user_id = %s
            """,
            (status, time_completed, task_id, user_id)
        )

def delete_task_repo(user_id:str, task_id:str):
    with get_cur() as cur:
        cur.execute(
            """
            DELETE FROM tasks 
            WHERE task_id = %s AND user_id = %s
            """,(task_id, user_id)
        )