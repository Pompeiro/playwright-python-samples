from playwright.sync_api import Page
from pages.base import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.resource_path = "/zaloguj"
        self.email_field = self.page.locator("#email")
        self.password_field = self.page.locator("#password")
        self.login_button = self.page.get_by_role("button", name="Zaloguj")
        self.password_validation_error = self.page.get_by_text("Adres e-mail i/lub hasło są niepoprawne.")
        self.forgot_password_link = self.page.get_by_role("link", name="Nie pamiętam hasła")

    def login(self, email: str, password: str) -> None:
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.login_button.click()

