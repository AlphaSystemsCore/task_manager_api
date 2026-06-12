from app.repositories.tasks_repo import ( 
    create_task_repo, 
    get_tasks_repo,
    get_task_by_name_repo,
    update_task_repo
    )
from app.schemas.task_schemas import TasksOut
def create_task_service(name: str, category:str, user_id:str , duration: str):
    
    try:
        task_id = create_task_repo(name, category, user_id , duration)
    except Exception as e:
        #log exception
        raise Exception("Can not create task")
    else:
        return task_id

def get_tasks_service(user_id, limit: int, offset: int):
    tasks = get_tasks_repo(user_id, limit, offset)
    
    if not tasks:
        raise Exception("No task Found")
    else:
        return [
                TasksOut(
                task_id=task[0],
                name=task[1],
                category=task[2],
                status=task[3],
                time_created=task[4],
                duration=task[5],
                time_completed=task[6]
            )
            for task in tasks]

def get_task_by_name_service(user_id, task_name):
    if not user_id:
        raise ValueError("Task Name can not be blank")
    task =  get_task_by_name_repo(user_id, task_name)
    if task is None:
        raise Exception(f"Task {task_name} not found")
    else:
        return TasksOut(
                task_id=task[0],
                name=task[1],
                category=task[2],
                status=task[3],
                time_created=task[4],
                duration=task[5],
                time_completed=task[6]
            )

def update_task_service(
    user_id:str,
    task_id:str,
    name: str|None = None,
    category:str| None = None,
    status:str|None = None,
    time_to_be_completed: str| None = None,
):  
    try:
        update_task_repo(
            user_id,
            task_id,
            name, 
            category,
            time_to_be_completed)

    except Exception as e:
        raise Exception