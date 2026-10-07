import json
from pathlib import Path
from typing import Dict, List


Task = Dict[str, object]


def load_tasks(path: Path) -> List[Task]:
    """Загружает список задач из JSON-файла."""
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as error:
        raise ValueError("Файл задач содержит некорректный JSON.") from error

    if not isinstance(data, list):
        raise ValueError("Корневой элемент JSON должен быть списком.")
    return data


def save_tasks(path: Path, tasks: List[Task]) -> None:
    """Сохраняет список задач в JSON-файл."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
