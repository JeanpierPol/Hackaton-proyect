import pytest  # type: ignore

from src.domain.repository.user_repository import UserRepository
from src.domain.interactor.user_interactor import UserInteractor
from src.domain.model.user import hash_password
import sqlite3



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

def test_current_user_should_return_user_if_logged(database):
    def fake_get_user_id():
        return "admin-1"

    user_repository = UserRepository(
        None, database, get_current_user_id=fake_get_user_id
    )
    interactor = UserInteractor(None, user_repository)

    user = interactor.get_current_user()
    assert user.user_id == "admin-1"
    assert user.username == "admin1"
    assert user.user_mail == "admin1@gmail.com"
    assert user.user_rol == "superadmin"

def test_current_user_should_return_None_if_not_logged(database):
    user_repository = UserRepository(None, database, lambda: None)
    interactor = UserInteractor(None, user_repository)

    assert interactor.get_current_user() is None


def test_current_user_should_return_None_if_not_id_getter_function(database):
    user_repository = UserRepository(None, database)
    interactor = UserInteractor(None, user_repository)

    assert interactor.get_current_user() is None
   



def test_current_user_should_return_user_if_logged(database):
    user_repository = UserRepository(None, database, lambda: "admin-1")
    interactor = UserInteractor(None, user_repository)

    user = interactor.get_current_user()
    assert user.user_id == "admin-1"
    assert user.username == "admin1"
    assert user.user_mail == "admin-1@example.com"
    assert user.user_rol == "superadmin"
    

def test_current_user_should_return_None_if_not_logged(database):
    user_repository = UserRepository(None, database, lambda: None)
    interactor = UserInteractor(None, user_repository)

    assert interactor.get_current_user() is None


# def test_current_user_should_return_None_if_not_id_getter_function(database):
#     user_repository = UserRepository(None, database)
#     interactor = UserInteractor(None, user_repository)

#     assert interactor.get_current_user() is None
