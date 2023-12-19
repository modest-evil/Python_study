from demoqa_fixtures import cleanup
from demoqa_fixtures import create_account
from demoqa_fixtures import create_and_log_in
from dotenv import load_dotenv
import os

load_dotenv()
test_username = os.getenv("USERNAME")
test_password = os.getenv("PASSWORD")


def test_create_account(cleanup):
    # user = User(url)

    # temp = cleanup.create_user(username, password)
    # status = temp["status"]
    #
    # assert status == 201

    assert cleanup.create_user(test_username, test_password)["status"] == 201


def test_generate_token(create_account):
    # user = User(url)
    #
    # user.create_user("Alan", "Alan123!")
    #
    # temp = user.log_in("Alan", "Alan123!")
    # temp = user.log_in(user.username, user.password)
    # status = temp["status"]
    #
    # assert status == 200

    user = create_account
    assert user.log_in(user.username, user.password)["status"] == 200


def test_is_logged_in(create_and_log_in):
    # user = User(url)
    #
    # user.create_user("Bene", "Bene123!")
    # user.log_in("Bene", "Bene123!")
    #
    # temp = user.is_logged_in("Bene", "Bene123!")
    # status = temp["status"]
    #
    # assert status == 200

    user = create_and_log_in
    assert user.is_logged_in(user.username, user.password)["status"] == 200


def test_get_user_info(create_and_log_in):
    # user = User(url)
    #
    # user.create_user("Cody", "Cody123!")
    # print(user.userId)
    #
    # user.log_in("Cody", "Cody123!")
    # print(user.sessionToken)
    #
    # temp = user.get_user_info(user.sessionToken, user.userId)
    # status = temp["status"]
    #
    # assert status == 200

    user = create_and_log_in
    assert user.get_user_info(user.sessionToken, user.userId)["status"] == 200


def test_delete_account(create_and_log_in):
    # user = User(url)
    #
    # user.create_user("Elon", "Elon123!")
    # user.log_in("Elon", "Elon123!")
    #
    # assert user.delete_account(user.sessionToken, user.userId) == 204

    user = create_and_log_in
    user.save_user = True
    assert user.delete_account(user.sessionToken, user.userId) == 204
