from playwright.sync_api import Page
from pages.base import BasePage

class DashboardPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.logout_button = self.page.get_by_title(text="Wyloguj")

    def logout(self) -> None:
        self.logout_button.click()


