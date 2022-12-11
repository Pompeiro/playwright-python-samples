import _pytest.fixtures
from playwright.sync_api import Page, expect

from pages.login import LoginPage
from pages.password_recovery import PasswordRecoveryPage


def test_someone_should_be_redirected_to_login_page_by_clicking_login(
    page: Page, request: _pytest.fixtures.FixtureRequest, debug_mode: bool
) -> None:

    password_recovery_page = PasswordRecoveryPage(page)
    login_page = LoginPage(page)
    password_recovery_page.navigate()
    password_recovery_page.make_debug_screenshot(
        node_id=request.node.nodeid, screenshot_name="Start", debug_mode=debug_mode
    )

    password_recovery_page.login_link.click()

    expect(page).to_have_url(login_page.combine_url())
    password_recovery_page.make_debug_screenshot(
        node_id=request.node.nodeid, screenshot_name="Stop", debug_mode=debug_mode
    )
