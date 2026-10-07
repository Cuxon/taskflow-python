from __future__ import annotations

from datetime import datetime


def input_int(prompt: str, minimum: int | None = None) -> int:
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                raise ValueError
            return value
        except ValueError:
            print("Введите корректное целое число.")


def input_date(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Дата должна иметь формат YYYY-MM-DD.")
