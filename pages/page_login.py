class LoginPage:
    def __init__(self, page):
        self.page = page
        self._username = page.locator("#user-name")
        self._password = page.locator("#password")
        self._login_btn = page.locator("#login-button")
        self._error_msg = page.locator("[data-test='error']")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self._username.fill(username)
        self._password.fill(password)
        self._login_btn.click()