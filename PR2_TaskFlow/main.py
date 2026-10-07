from pathlib import Path

from storage import load_tasks, save_tasks
from tasks import create_task, find_tasks, mark_task_completed, sort_tasks_by_priority
from utils import next_task_id, print_tasks


DATA_FILE = Path(__file__).parent / "data" / "tasks.json"


def run_demo() -> None:
    """Запускает демонстрационный сценарий ПР2."""
    tasks = load_tasks(DATA_FILE)

    if not tasks:
        tasks = [
            create_task(1, "Подготовить отчет по ПР1", 5, 4, 3),
            create_task(2, "Подготовить проект по Python", 4, 5, 7),
            create_task(3, "Повторить вопросы к защите", 3, 2, 5),
        ]
        save_tasks(DATA_FILE, tasks)

    print("=== TaskFlow: ПР2 ===")
    print("\nВсе задачи:")
    print_tasks(tasks)

    print("\nЗадачи с приоритетом:")
    prioritized = sort_tasks_by_priority(tasks)
    print_tasks(prioritized)

    print("\nРезультат поиска 'Python':")
    print_tasks(find_tasks(tasks, "Python"))

    completed_id = next_task_id(tasks) - 1
    mark_task_completed(tasks, completed_id)
    save_tasks(DATA_FILE, tasks)
    print(f"\nЗадача №{completed_id} отмечена выполненной.")


if __name__ == "__main__":
    run_demo()
