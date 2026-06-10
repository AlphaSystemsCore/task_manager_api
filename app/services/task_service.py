from app.repositories.tasks_repo import create_task_repo, get_all_tasks_repo, get_task_by_name_repo
def create_task_service(name: str, category:str, user_id:str , duration: str):
    try:
        task_id = create_task_repo(name, category, user_id , duration)
        return task_id
    except Exception as e:
        print(e)

def get_all_tasks_service(user_id, limit: int, offset: int):
    tasks = get_all_tasks_repo(user_id, limit, offset)
    if tasks is not None:
        return tasks
    else:
        return []

def get_task_by_name_service(user_id, name):
    task = get_task_by_name_repo(user_id, name)
    print(task)

    if task:
        return task
    else:
        return []
