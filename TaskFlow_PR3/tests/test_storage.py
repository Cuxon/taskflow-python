from pathlib import Path

from models import Task, User
from storage import load_tasks, load_users, save_tasks, save_users


def test_tasks_json_roundtrip(tmp_path: Path) -> None:
    path = tmp_path / "tasks.json"
    tasks = [Task(1, "Test", priority="высокий")]
    save_tasks(path, tasks)
    loaded = load_tasks(path)
    assert len(loaded) == 1
    assert isinstance(loaded[0], Task)
    assert loaded[0].title == "Test"


def test_users_json_roundtrip(tmp_path: Path) -> None:
    path = tmp_path / "users.json"
    users = [User(1, "Иван", "ivan@example.com")]
    save_users(path, users)
    loaded = load_users(path)
    assert isinstance(loaded[0], User)
    assert loaded[0].email == "ivan@example.com"
