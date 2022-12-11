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
