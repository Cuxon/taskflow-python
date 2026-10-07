import pytest

from models import User


def test_user_str_and_attributes() -> None:
    user = User(1, "Иван", "ivan@example.com")
    assert user.name == "Иван"
    assert "ivan@example.com" in str(user)


def test_invalid_email() -> None:
    with pytest.raises(ValueError):
        User(1, "Иван", "invalid")
