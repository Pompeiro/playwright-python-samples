from playwright.sync_api import Page, expect

from pages.tasks import TasksPage


def test_user_can_navigate_to_tasks(
    page_with_user: Page, user_email: str, user_password: str
) -> None:
    tasks_page = TasksPage(page_with_user)
    tasks_page.navigate()
    expect(page_with_user).to_have_url(tasks_page.combine_url())
