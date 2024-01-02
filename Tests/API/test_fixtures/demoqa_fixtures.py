import pytest

from Tests.API.test_helpers.user_funcs import User
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("URL")
test_username = os.getenv("USERNAME")
test_password = os.getenv("PASSWORD")

@pytest.fixture
def cleanup():
    user = User(url)
    yield user

    if not (user.is_logged_in(user.username, user.password)["body"]):
        user.log_in(user.username, user.password)

    if not user.save_user:
        user.delete_account(user.sessionToken, user.userId)


@pytest.fixture(params=[(test_username, test_password)])
def create_account(request, cleanup):
    # cleanup.create_user("Dori", "Dori123!")
    username, password = request.param
    cleanup.create_user(username, password)

    yield cleanup


@pytest.fixture(params=[(test_username, test_password)])
def create_and_log_in(request, cleanup):
    username, password = request.param
    cleanup.create_user(username, password)
    cleanup.log_in(username, password)

    yield cleanup
