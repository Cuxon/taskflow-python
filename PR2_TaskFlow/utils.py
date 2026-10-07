from typing import List


def print_tasks(tasks: List[dict]) -> None:
    """Выводит задачи в компактном виде."""
    if not tasks:
        print("Задач нет.")
        return

    for task in tasks:
        state = "готово" if task["completed"] else "активна"
        print(
            f'{task["id"]}. {task["name"]} | '
            f'важность: {task["importance"]} | '
            f'срочность: {task["urgency"]} | '
            f'до: {task["deadline"]} | {state}'
        )


def next_task_id(tasks: List[dict]) -> int:
    """Возвращает следующий свободный идентификатор."""
    if not tasks:
        return 1
    return max(int(task["id"]) for task in tasks) + 1
