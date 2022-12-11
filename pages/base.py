from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_url = "http://demo.testarena.pl"
        self.resource_path = "/"


    def combine_url(self) ->str:
        return self.base_url + self.resource_path

    def navigate(self) -> None:
        self.page.goto(self.combine_url())

    def make_debug_screenshot(self, node_id:str, screenshot_name:str, debug_mode:bool=False) -> None:
        """
        test_node_id: 'tests/testarena/test_password_recovery.py::test_is_redirected_to_login_page_by_clicking_login[chromium]'
        test_name: test_is_redirected_to_login_page_by_clicking_login[chromium]
        """
        test_name = node_id[node_id.find("::") + 2:]
        if debug_mode:
            self.page.screenshot(path="screenshots/"+test_name +"/" + screenshot_name + ".jpg",full_page=True)