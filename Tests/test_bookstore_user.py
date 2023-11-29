import json

from user_funcs import User


def test_create_account():
    user = User("https://demoqa.com")

    temp = user.create_user("Dori", "Dori123!")
    status = temp["status"]

    assert status == 201


def test_generate_token():
    user = User("https://demoqa.com")

    user.create_user("Alan", "Alan123!")

    temp = json.loads(str(user.log_in("Alan", "Alan123!")).replace("'", '"'))
    status = temp["status"]

    assert status == 200


def test_is_logged_in():
    user = User("https://demoqa.com")

    user.create_user("Bene", "Bene123!")
    user.log_in("Bene", "Bene123!")

    print(user.is_logged_in("Bene", "Bene123!"))

    temp = json.loads(str(user.is_logged_in("Bene", "Bene123!")).replace("'", '"'))
    status = temp["status"]

    assert status == 200


def test_get_user_info():
     user = User("https://demoqa.com")

     temp = user.create_user("Cody", "Cody123!")
     #result = json.loads(str(temp["body"]).replace("'", '"'))
     print(user.userId)
     # userId = result["userID"]
     # print(userId)

     temp = user.log_in("Cody", "Cody123!")
     print(user.sessionToken)
     # result = json.loads(str(temp["body"]).replace("'", '"'))
     # sessionToken = result["token"]
     # print(sessionToken)

     temp = json.loads(str(user.get_user_info(user.sessionToken, user.userId)).replace("'", '"'))
     status = temp["status"]

     assert status == 200


def test_delete_account():
    user = User("https://demoqa.com")

    temp = json.loads(str(user.create_user("Elon", "Elon123!")).replace("'", '"'))
    result = json.loads(str(temp["body"]).replace("'", '"'))
    userId = result["userID"]

    temp = json.loads(str(user.log_in("Elon", "Elon123!")).replace("'", '"'))
    result = json.loads(str(temp["body"]).replace("'", '"'))
    sessionToken = result["token"]

   # print(user.delete_account(sessionToken, userId))

    # temp = json.loads(str(user.delete_account(sessionToken, userId)).replace("'", '"'))
    # status = temp["status"]

    assert user.delete_account(sessionToken, userId) == 204



