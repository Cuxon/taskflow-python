from models import Task
from tasks import create_task, find_tasks, sort_by_priority


def test_create_task_adds_object() -> None:
    tasks: list[Task] = []
    task = create_task(tasks, "Новая задача", priority="высокий")
    assert len(tasks) == 1
    assert tasks[0] is task
    assert task.id == 1


def test_find_tasks() -> None:
    tasks = [
        Task(1, "Python", "ООП"),
        Task(2, "Базы данных", "SQL"),
    ]
    result = find_tasks(tasks, "ооп")
    assert [task.id for task in result] == [1]


def test_sort_by_priority() -> None:
    tasks = [
        Task(1, "A", priority="низкий"),
        Task(2, "B", priority="высокий"),
        Task(3, "C", priority="средний"),
    ]
    result = sort_by_priority(tasks)
    assert [task.priority for task in result] == ["высокий", "средний", "низкий"]
