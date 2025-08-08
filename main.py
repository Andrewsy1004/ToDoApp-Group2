# main.py
from app.models.task_model import TaskModel

def main():
    task = TaskModel("Estudiar para el examen")
    print(f"Tarea creada: {task.get_task_name()}")
    task.mark_as_complete()
    print(f"Tarea completada (mark_as_complete): {task.is_completed()}")
    task.set_done()
    print(f"Tarea completada (set_done): {task.is_completed()}")
    task.delete_task()
    print(f"Tarea eliminada (delete_task): {task.get_task_name()}")
    task.remove_task()
    print(f"Tarea eliminada (remove_task): {task.get_task_name()}")

if __name__ == "__main__":
    main()
