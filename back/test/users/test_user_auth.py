import pytest  # type: ignore

from src.domain.repository.user_repository import UserRepository
from src.domain.interactor.user_interactor import UserInteractor

import sqlite3

from src.domain.model.user import hash_password
from src.lib.errors import NotAuthorizedError


@pytest.fixture
def database():
    conn = sqlite3.connect(":memory:")
    conn.executescript(
        f"""
        DROP TABLE IF EXISTS users;
        CREATE TABLE users (
            id varchar primary key,
            username varchar,
            name varchar,
            password varchar,
            is_admin boolean
        );
        INSERT INTO users ( id, username, name, password, is_admin) values 
            ("user-1", "user-1@example.com", "User 1", '{hash_password("user-1-password")}', 1),
            ("user-2", "user-2@example.com", "User 2", '{hash_password("user-2-password")}', 0),
            ("user-3", "user-3@example.com", "User 3", '{hash_password("user-3-password")}', 0),
            ("user-4", "user-4@example.com", "User 4", '{hash_password("user-4-password")}', 0);
        """
    )
    return conn


def test_auth_user_should_return_user_if_password_is_ok(database):
    user_repository = UserRepository(None, database, lambda: "user-1")
    interactor = UserInteractor(None, user_repository)

    user = interactor.auth_user("user-1@example.com", "user-1-password")
    assert user.id == "user-1"
    assert user.username == "user-1@example.com"
    assert user.name == "User 1"
    assert user.is_admin is True


def test_auth_user_should_raises_unauthorized_if_user_is_unknown(database):
    user_repository = UserRepository(None, database, lambda: "user-1")
    interactor = UserInteractor(None, user_repository)

    with pytest.raises(NotAuthorizedError):
        interactor.auth_user("user-unknown@example.com", "user-1-bad-password")


def test_auth_user_should_raises_unauthorized_if_password_not_ok(database):
    user_repository = UserRepository(None, database, lambda: "user-1")
    interactor = UserInteractor(None, user_repository)

    with pytest.raises(NotAuthorizedError):
        interactor.auth_user("user-1@example.com", "user-1-bad-password")
