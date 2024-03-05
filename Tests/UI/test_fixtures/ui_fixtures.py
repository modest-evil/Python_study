import pytest

from Tests.API.test_helpers.user_funcs import User
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("URL")
test_username = os.getenv("TESTUSER")
test_password = os.getenv("PASSWORD")

@pytest.fixture()
def before_test(page):
    user = User(url)
    yield user

    if not (user.is_logged_in(user.username, user.password)["body"]):
        user.log_in(user.username, user.password)

    else :
        session_storage = page.evaluate("() => JSON.stringify(sessionStorage)")
        os.environ["SESSION_STORAGE"] = session_storage
        # user.userId = session_storage.
        # user.sessionToken = session_storage.

    if not user.save_user:
        user.delete_account(user.sessionToken, user.userId)


@pytest.fixture(params=[(test_username, test_password)])
def user_exists(request, before_test, page):
    username, password = request.param
    before_test.create_user(username, password)

    yield before_test


@pytest.fixture(params=[(test_username, test_password)])
def user_logged_in(request, before_test, page):
    username, password = request.param
    before_test.create_user(username, password)
    before_test.log_in(username, password)

    yield before_test
