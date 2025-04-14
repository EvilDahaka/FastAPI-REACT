import pytest
from pydantic import ValidationError
from schemas.users import UserLogin

def test_user_login_valid_data():
    data = {"email": "test@mail.com", "password": "securepassword123"}
    user_login = UserLogin(**data)
    assert user_login.email == data["email"]
    assert user_login.password == data["password"]


def test_user_login_invalid_email():
    data = {"email": "invalid-email", "password": "securepassword123"}
    with pytest.raises(ValidationError):
        UserLogin(**data)


def test_user_login_missing_password():
    data = {"email": "test@mail.com"}
    with pytest.raises(ValidationError):
        UserLogin(**data)


def test_user_login_missing_email():
    data = {"password": "securepassword123"}
    with pytest.raises(ValidationError):
        UserLogin(**data)