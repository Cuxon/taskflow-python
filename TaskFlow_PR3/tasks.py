from __future__ import annotations

from typing import Iterable

from models import Task


def add_task(tasks: list[Task], task: Task) -> None:
    """Добавить задачу в коллекцию."""
    if any(item.id == task.id for item in tasks):
        raise ValueError("Задача с таким ID уже существует.")
    tasks.append(task)


def create_task(
    tasks: list[Task],
    title: str,
    description: str = "",
    priority: str = "средний",
    due_date: str | None = None,
    user_id: int | None = None,
) -> Task:
    """Создать и добавить задачу с автоматически выбранным ID."""
    next_id = max((task.id for task in tasks), default=0) + 1
    task = Task(next_id, title, description, priority, "новая", due_date, user_id)
    add_task(tasks, task)
    return task


def find_tasks(tasks: Iterable[Task], query: str) -> list[Task]:
    """Найти задачи по части названия или описания."""
    query = query.lower().strip()
    return [
        task for task in tasks
        if query in task.title.lower() or query in task.description.lower()
    ]


def filter_by_status(tasks: Iterable[Task], status: str) -> list[Task]:
    return [task for task in tasks if task.status == status]


def sort_by_priority(tasks: Iterable[Task]) -> list[Task]:
    order = {"высокий": 0, "средний": 1, "низкий": 2}
    return sorted(tasks, key=lambda task: order[task.priority])


def change_task_status(tasks: Iterable[Task], task_id: int, status: str) -> bool:
    """Изменить статус найденной задачи."""
    for task in tasks:
        if task.id == task_id:
            task.change_status(status)
            return True
    return False


def get_overdue_tasks(tasks: Iterable[Task]) -> list[Task]:
    return [task for task in tasks if task.is_overdue()]
