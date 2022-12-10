from playwright.sync_api import Page, expect

from pages.login import LoginPage
from pages.password_recovery import PasswordRecoveryPage


def test_is_redirected_to_login_page_by_clicking_login(page: Page) -> None:
    password_recovery_page = PasswordRecoveryPage(page)
    login_page = LoginPage(page)
    password_recovery_page.navigate()

    password_recovery_page.login_link.click()

    expect(page).to_have_url(login_page.combine_url())
