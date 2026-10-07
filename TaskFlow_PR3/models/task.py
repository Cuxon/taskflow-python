from __future__ import annotations

from datetime import date
from typing import Any


class Task:
    """Учебная задача TaskFlow."""

    STATUSES = {"новая", "в работе", "выполнена"}
    PRIORITIES = {"низкий", "средний", "высокий"}

    def __init__(
        self,
        task_id: int,
        title: str,
        description: str = "",
        priority: str = "средний",
        status: str = "новая",
        due_date: str | None = None,
        user_id: int | None = None,
    ) -> None:
        if priority not in self.PRIORITIES:
            raise ValueError("Некорректный приоритет.")
        if status not in self.STATUSES:
            raise ValueError("Некорректный статус.")
        self.id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.due_date = due_date
        self.user_id = user_id

    def change_status(self, status: str) -> None:
        """Изменить статус задачи."""
        if status not in self.STATUSES:
            raise ValueError("Некорректный статус.")
        self.status = status

    def is_overdue(self, today: date | None = None) -> bool:
        """Проверить, просрочена ли невыполненная задача."""
        if not self.due_date or self.status == "выполнена":
            return False
        current = today or date.today()
        return date.fromisoformat(self.due_date) < current

    def __str__(self) -> str:
        return (
            f"[{self.id}] {self.title} | "
            f"приоритет: {self.priority} | статус: {self.status}"
        )

    def to_dict(self) -> dict[str, Any]:
        """Преобразовать объект в структуру для JSON."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "due_date": self.due_date,
            "user_id": self.user_id,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Task":
        """Создать объект из JSON-данных."""
        return cls(
            task_id=int(data["id"]),
            title=str(data["title"]),
            description=str(data.get("description", "")),
            priority=str(data.get("priority", "средний")),
            status=str(data.get("status", "новая")),
            due_date=data.get("due_date"),
            user_id=data.get("user_id"),
        )
