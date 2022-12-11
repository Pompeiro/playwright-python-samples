import pytest
from playwright.sync_api import Page

from pages.login import LoginPage


@pytest.fixture()
def user_email() -> str:
    return "administrator@testarena.pl"


@pytest.fixture()
def user_password() -> str:
    return "sumXQQ72$L"


@pytest.fixture(scope="session")
def browser_context_args(  # pylint: disable=unused-argument, redefined-outer-name
    browser_context_args, playwright
) -> dict:
    return {"viewport": {"width": 1920, "height": 1080}}


@pytest.fixture()
def page_with_user(  # pylint: disable=redefined-outer-name
    page: Page,
    user_email: str,
    user_password: str,
) -> Page:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(email=user_email, password=user_password)
    return page
