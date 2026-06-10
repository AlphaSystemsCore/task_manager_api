from app.repositories.tasks_repo import ( 
    create_task_repo, 
    get_tasks_repo
    )

def create_task_service(name: str, category:str, user_id:str , duration: str):
    try:
        task_id = create_task_repo(name, category, user_id , duration)
    except Exception as e:
        #log exception
        raise Exception
    else:
        return task_id

def get_tasks_service(user_id, limit: int, offset: int):
    # tasks = get_tasks_repo(user_id, limit, offset)
    tasks = []
    if not tasks:
        return None
    else:
        return tasks
