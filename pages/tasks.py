from playwright.sync_api import Page
from pages.base import BasePage

class TasksPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.resource_path = "/testyb/tasks"
        self.task_add_link = page.get_by_role("link", name="Dodaj zadanie")


