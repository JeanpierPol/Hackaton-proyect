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
        DROP TABLE IF EXISTS user;
        CREATE TABLE user (
            user_id	TEXT,
            username	TEXT NOT NULL,
            password	TEXT,
            user_mail	TEXT UNIQUE,
            user_rol	TEXT,
            user_status	BOOLEAN,
            user_surename	INTEGER,
            PRIMARY KEY(user_id)
   );
        INSERT INTO user ( user_id, username, password,user_mail,user_rol,user_status,user_surename) values 
            ("admin-1","admin1",'{hash_password("admin1111")}' ,"admin-1@example.com","superadmin",1,"admin-surename" ),
            ("user-2","admin2",'{hash_password("admin2222")}'  ,"admin-2@example.com","admin",1,"admin2-surename" ),
            ("user-3","user1",'{hash_password("user1111")}'  ,"user-1@example.com", "user",1,"user1-surename" ),
            ("user-4","user2",'{hash_password("user2222")}' ,"user-2@example.com", "user",1,"user2-surename" );
        """
    )
    return conn


def test_auth_user_should_return_user_if_password_is_ok(database):
    user_repository = UserRepository(None, database, lambda: "admin-1")
    interactor = UserInteractor(None, user_repository)

    user = interactor.auth_user("admin1", "admin1111")
    assert user.user_id == "admin-1"
    assert user.username == "admin1"
    assert user.user_rol == "superadmin"


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