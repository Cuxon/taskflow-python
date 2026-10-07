from __future__ import annotations

from typing import Iterable

from models import User


def add_user(users: list[User], user: User) -> None:
    if any(item.id == user.id for item in users):
        raise ValueError("Пользователь с таким ID уже существует.")
    users.append(user)


def create_user(users: list[User], name: str, email: str) -> User:
    next_id = max((user.id for user in users), default=0) + 1
    user = User(next_id, name, email)
    add_user(users, user)
    return user


def find_user(users: Iterable[User], query: str) -> list[User]:
    query = query.lower().strip()
    return [
        user for user in users
        if query in user.name.lower() or query in user.email.lower()
    ]
