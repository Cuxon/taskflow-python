from datetime import date

import pytest

from models import Task


def test_task_attributes_and_str() -> None:
    task = Task(1, "ООП", priority="высокий")
    assert task.id == 1
    assert "ООП" in str(task)
    assert "высокий" in str(task)


def test_change_status() -> None:
    task = Task(1, "ООП")
    task.change_status("в работе")
    assert task.status == "в работе"


def test_invalid_status() -> None:
    with pytest.raises(ValueError):
        Task(1, "ООП", status="ошибка")


def test_overdue_task() -> None:
    task = Task(1, "Сдать", due_date="2026-10-01")
    assert task.is_overdue(date(2026, 10, 7))


def test_completed_task_is_not_overdue() -> None:
    task = Task(1, "Сдать", status="выполнена", due_date="2026-10-01")
    assert not task.is_overdue(date(2026, 10, 7))


def test_json_conversion() -> None:
    original = Task(3, "Тест", "Описание", "низкий", "новая", "2026-11-01", 2)
    restored = Task.from_dict(original.to_dict())
    assert restored.id == original.id
    assert restored.title == original.title
    assert restored.priority == original.priority
