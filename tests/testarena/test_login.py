from playwright.sync_api import Page, expect

from pages.dashboard import DashboardPage
from pages.login import LoginPage
from pages.password_recovery import PasswordRecoveryPage


def test_someone_can_login_with_valid_credentials(
    page: Page, user_email: str, user_password: str
) -> None:
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    login_page.navigate()

    login_page.login(email=user_email, password=user_password)

    expect(page).to_have_url(dashboard_page.combine_url())
    expect(dashboard_page.logout_button).to_be_visible()


def test_someone_can_not_login_with_invalid_credentials(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()

    login_page.login(email="invalid@email.com", password="invalid")

    expect(login_page.password_validation_error).to_be_visible()


def test_email_address_filled_with_invalid_email_format_triggers_error(
    page: Page,
) -> None:
    login_page = LoginPage(page)
    login_page.navigate()

    login_page.login(email="invalid", password="invalid")

    expect(login_page.password_validation_error).to_be_visible()


def test_is_redirected_to_password_recovery_page_by_clicking_forgot_password(
    page: Page,
) -> None:
    login_page = LoginPage(page)
    password_recovery_page = PasswordRecoveryPage(page)
    login_page.navigate()

    login_page.forgot_password_link.click()

    expect(page).to_have_url(password_recovery_page.combine_url())
