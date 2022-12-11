from playwright.sync_api import Page, expect
from pages.base import BasePage

class TaskViewPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.resource_path = "/testyb/task_view/id"
        self.title = page.locator("#text.content_label_title")

    def expect_title_and_description(self, title:str, description: str) -> None:
        expect(self.title).to_contain_text(title)
        expect(self.page.get_by_text(description)).to_be_visible()