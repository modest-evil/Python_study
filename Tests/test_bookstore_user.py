import json

import pytest

from demoqa_functions import Demoqa
from user_funcs import User
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("URL")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")


@pytest.fixture#(params=[(user.delete_account = True)]
def cleanup():
    user = User(url)
    yield user

    if not (user.is_logged_in(user.username, user.password)["body"]):
        user.log_in(user.username, user.password)

   # user.delete_account(user.sessionToken, user.userId)
    if not user.save_user:
        user.delete_account(user.sessionToken, user.userId)


@pytest.fixture(params=[(username, password)])
def create_account(request, cleanup):
    # cleanup.create_user("Dori", "Dori123!")
    username, password = request.param
    cleanup.create_user(username, password)

    yield cleanup


def test_create_account(cleanup):
    # user = User(url)

    temp = cleanup.create_user(username, password)
    status = temp["status"]

    assert status == 201


def test_generate_token(create_account):
    user = create_account
    # user = User(url)
    #
    # user.create_user("Alan", "Alan123!")
    #
    # temp = user.log_in("Alan", "Alan123!")
    temp = user.log_in(user.username, user.password)
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


def test_delete_account(cleanup):
    user = User(url)

    user.create_user("Elon", "Elon123!")
    user.log_in("Elon", "Elon123!")

    assert user.delete_account(user.sessionToken, user.userId) == 204
