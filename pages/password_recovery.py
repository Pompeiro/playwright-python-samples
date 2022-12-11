from playwright.sync_api import Page
from pages.base import BasePage

class PasswordRecoveryPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.resource_path = "/odzyskaj_haslo"
        self.email_field = self.page.locator("#email")
        self.recover_password_button = self.page.get_by_role("button", name="Odzyskaj hasło")
        self.captcha_checkbox = self.page.get_by_role("checkbox", name="Nie jestem robotem")
        self.login_link = self.page.get_by_role("link", name="Strona logowania")

    def recover_password(self, email: str) -> None:
        self.email_field.fill(email)
        self.captcha_checkbox.click()
        self.recover_password_button.click()