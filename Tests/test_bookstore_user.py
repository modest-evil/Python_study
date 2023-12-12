import json

from demoqa_functions import Demoqa
from user_funcs import User
from dotenv import load_dotenv
import os


load_dotenv()
url = os.getenv("URL")


def test_create_account():
    user = User(url)

    temp = user.create_user("Dori", "Dori123!")
    status = temp["status"]

    assert status == 201


def test_generate_token():
    user = User(url)

    user.create_user("Alan", "Alan123!")

    temp = user.log_in("Alan", "Alan123!")
    status = temp["status"]

    assert status == 200


def test_is_logged_in():
    user = User(url)

    user.create_user("Bene", "Bene123!")
    user.log_in("Bene", "Bene123!")

    temp = user.is_logged_in("Bene", "Bene123!")
    status = temp["status"]

    assert status == 200


def test_get_user_info():
     user = User(url)

     user.create_user("Cody", "Cody123!")
     print(user.userId)

     user.log_in("Cody", "Cody123!")
     print(user.sessionToken)

     temp = user.get_user_info(user.sessionToken, user.userId)
     status = temp["status"]

     assert status == 200


def test_delete_account():
    user = User(url)

    user.create_user("Elon", "Elon123!")
    user.log_in("Elon", "Elon123!")

    assert user.delete_account(user.sessionToken, user.userId) == 204



