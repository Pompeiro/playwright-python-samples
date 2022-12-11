from playwright.sync_api import Page

from pages.task_add import TaskAddPage
from pages.task_view import TaskViewPage


def test_user_should_create_task_by_filling_all_required_fields_with_valid_data(
    page_with_user: Page,
) -> None:
    title = "Task 2138"
    description = "Best task ever"
    environment = "env"
    version = "ver"
    task_add_page = TaskAddPage(page_with_user)
    task_view_page = TaskViewPage(page_with_user)
    task_add_page.navigate()

    task_add_page.create_task(
        title=title, description=description, environment=environment, version=version
    )

    task_view_page.expect_title_and_description(title=title, description=description)
    # some kind of teardown could be a next step
