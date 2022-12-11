from playwright.sync_api import Page, Locator
from pages.base import BasePage

class TaskAddPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.resource_path = "/testyb/task_add"
        self.title_field = page.locator("#title")
        self.description_field = page.locator("#description")
        self.environments_field = page.locator("#token-input-environments")
        self.versions_field = page.locator("#token-input-versions")
        self.date_picker = page.locator("#dueDate")
        self.date_picker_23th_day = page.get_by_role("link", name="23")
        self.date_picker_ready_button = page.get_by_role("button", name="Gotowe")
        self.assign_to_me_link = page.get_by_role("link", name="Przypisz do mnie")
        self.save_button = page.get_by_role("button", name="Zapisz")


    def create_task(self, title:str,description:str,environment:str,version:str) -> None:
        self.title_field.fill(title)
        self.description_field.fill(description)
        self._focus_search_field_and_fill(field=self.environments_field, text=environment)
        self._focus_search_field_and_fill(field=self.versions_field, text=version)
        self._pick_23th_day_in_date_picker()
        self.assign_to_me_link.click()
        self.save_button.click()

    def _focus_search_field_and_fill(self, field:Locator, text:str) -> None:
        field.click()
        field.fill(text)
        field.press("Backspace")
        self.page.get_by_role("listitem").filter(has_text=text).nth(1).click()

    def _pick_23th_day_in_date_picker(self) -> None:
        self.date_picker.click()
        self.date_picker_23th_day.click()
        self.date_picker_ready_button.click()
