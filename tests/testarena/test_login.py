import _pytest.fixtures
from playwright.sync_api import Page, expect

from pages import DashboardPage, LoginPage, PasswordRecoveryPage


def test_someone_can_login_with_valid_credentials(
    page: Page,
    user_email: str,
    user_password: str,
    request: _pytest.fixtures.FixtureRequest,
    debug_mode: bool,
) -> None:
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    login_page.navigate()
    login_page.make_debug_screenshot(
        node_id=request.node.nodeid, screenshot_name="Start", debug_mode=debug_mode
    )

    login_page.login(email=user_email, password=user_password)

    expect(page).to_have_url(dashboard_page.combine_url())
    expect(dashboard_page.logout_button).to_be_visible()
    login_page.make_debug_screenshot(
        node_id=request.node.nodeid, screenshot_name="Stop", debug_mode=debug_mode
    )


def test_someone_can_not_login_with_invalid_credentials(
    page: Page, request: _pytest.fixtures.FixtureRequest, debug_mode: bool
) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.make_debug_screenshot(
        node_id=request.node.nodeid, screenshot_name="Start", debug_mode=debug_mode
    )

    login_page.login(email="invalid@email.com", password="invalid")

    expect(login_page.password_validation_error).to_be_visible()
    login_page.make_debug_screenshot(
        node_id=request.node.nodeid, screenshot_name="Stop", debug_mode=debug_mode
    )


def test_email_address_filled_with_invalid_email_format_triggers_error(
    page: Page, request: _pytest.fixtures.FixtureRequest, debug_mode: bool
) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.make_debug_screenshot(
        node_id=request.node.nodeid, screenshot_name="Start", debug_mode=debug_mode
    )

    login_page.login(email="invalid", password="invalid")

    expect(login_page.password_validation_error).to_be_visible()
    login_page.make_debug_screenshot(
        node_id=request.node.nodeid, screenshot_name="Stop", debug_mode=debug_mode
    )


def test_someone_should_be_redirected_to_password_recovery_page_after_clicking_forgot_password_link(
    page: Page, request: _pytest.fixtures.FixtureRequest, debug_mode: bool
) -> None:
    login_page = LoginPage(page)
    password_recovery_page = PasswordRecoveryPage(page)
    login_page.navigate()
    login_page.make_debug_screenshot(
        node_id=request.node.nodeid, screenshot_name="Start", debug_mode=debug_mode
    )

    login_page.forgot_password_link.click()

    expect(page).to_have_url(password_recovery_page.combine_url())
    login_page.make_debug_screenshot(
        node_id=request.node.nodeid, screenshot_name="Stop", debug_mode=debug_mode
    )
