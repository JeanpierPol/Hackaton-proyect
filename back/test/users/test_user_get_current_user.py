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
            ("user-1", "user-1@example.com", "User 1", '{hash_password("user-1-passwd")}', 1),
            ("user-2", "user-2@example.com", "User 2", '{hash_password("user-2-passwd")}', 0),
            ("user-3", "user-3@example.com", "User 3", '{hash_password("user-3-passwd")}', 0),
            ("user-4", "user-4@example.com", "User 4", '{hash_password("user-4-passwd")}', 0);
        """
    )
    return conn


def test_current_user_should_return_user_if_logged(database):
    user_repository = UserRepository(None, database, lambda: "user-1")
    interactor = UserInteractor(None, user_repository)

    user = interactor.get_current_user()
    assert user.id == "user-1"
    assert user.username == "user-1@example.com"
    assert user.name == "User 1"
    assert user.is_admin is True


def test_current_user_should_return_None_if_not_logged(database):
    user_repository = UserRepository(None, database, lambda: None)
    interactor = UserInteractor(None, user_repository)

    assert interactor.get_current_user() is None


def test_current_user_should_return_None_if_not_id_getter_function(database):
    user_repository = UserRepository(None, database)
    interactor = UserInteractor(None, user_repository)

    assert interactor.get_current_user() is None
