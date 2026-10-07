from datetime import date, timedelta

from tasks import (
    calculate_deadline,
    calculate_priority,
    create_task,
    find_tasks,
    mark_task_completed,
    sort_tasks_by_priority,
)


def test_calculate_priority():
    assert calculate_priority(5, 5) == "Высокий"
    assert calculate_priority(3, 3) == "Средний"
    assert calculate_priority(1, 2) == "Низкий"


def test_calculate_deadline():
    start = date(2026, 10, 7)
    assert calculate_deadline(start, 7) == date(2026, 10, 14)


def test_create_task():
    task = create_task(1, "Тестовая задача", 4, 5, 2)
    assert task["name"] == "Тестовая задача"
    assert task["completed"] is False


def test_find_tasks():
    tasks = [
        {"id": 1, "name": "Python", "importance": 1, "urgency": 1},
        {"id": 2, "name": "Django", "importance": 1, "urgency": 1},
    ]
    assert len(find_tasks(tasks, "python")) == 1


def test_mark_task_completed():
    tasks = [{"id": 1, "name": "A", "completed": False}]
    assert mark_task_completed(tasks, 1) is True
    assert tasks[0]["completed"] is True


def test_sort_tasks_by_priority():
    tasks = [
        {"id": 1, "name": "Low", "importance": 1, "urgency": 1},
        {"id": 2, "name": "High", "importance": 5, "urgency": 5},
    ]
    result = sort_tasks_by_priority(tasks)
    assert result[0]["id"] == 2
