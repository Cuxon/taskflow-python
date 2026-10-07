from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models import Task, User


def load_json(path: str | Path, default: Any) -> Any:
    file_path = Path(path)
    if not file_path.exists():
        return default
    try:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError) as exc:
        raise ValueError(f"Не удалось прочитать {file_path}") from exc


def save_json(path: str | Path, data: Any) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    except OSError as exc:
        raise ValueError(f"Не удалось сохранить {file_path}") from exc


def load_tasks(path: str | Path) -> list[Task]:
    return [Task.from_dict(item) for item in load_json(path, [])]


def save_tasks(path: str | Path, tasks: list[Task]) -> None:
    save_json(path, [task.to_dict() for task in tasks])


def load_users(path: str | Path) -> list[User]:
    return [User.from_dict(item) for item in load_json(path, [])]


def save_users(path: str | Path, users: list[User]) -> None:
    save_json(path, [user.to_dict() for user in users])
