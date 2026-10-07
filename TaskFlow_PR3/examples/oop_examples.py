"""Небольшие примеры по темам ПР3."""


class Animal:
    """Базовый класс для демонстрации наследования и полиморфизма."""

    def speak(self) -> str:
        return "..."


class Dog(Animal):
    def speak(self) -> str:
        return "Гав!"


class Cat(Animal):
    def speak(self) -> str:
        return "Мяу!"


def log_call(func):
    """Пример простого декоратора."""
    def wrapper(*args, **kwargs):
        print(f"Вызов: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


class Calculator:
    """Пример staticmethod и classmethod."""

    factor = 1

    def __init__(self, value: int) -> None:
        self.value = value

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @classmethod
    def with_double_value(cls, value: int) -> "Calculator":
        return cls(value * 2)


if __name__ == "__main__":
    animals = [Dog(), Cat()]
    for animal in animals:
        print(animal.speak())

    print(Calculator.add(2, 3))
    print(Calculator.with_double_value(5).value)
