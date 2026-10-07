from __future__ import annotations

from typing import Any


class User:
    """Пользователь TaskFlow."""

    def __init__(self, user_id: int, name: str, email: str) -> None:
        if not name.strip():
            raise ValueError("Имя пользователя не может быть пустым.")
        if "@" not in email:
            raise ValueError("Некорректный email.")
        self.id = user_id
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"[{self.id}] {self.name} <{self.email}>"

    def to_dict(self) -> dict[str, Any]:
        return {"id": self.id, "name": self.name, "email": self.email}

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "User":
        return cls(int(data["id"]), str(data["name"]), str(data["email"]))
