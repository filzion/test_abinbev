from page_objects import PageElement, PageObject


class LoginPage(PageObject):
    username_input = PageElement(xpath='//*[@id="user"]')
    password_input = PageElement(xpath='//*[@id="pass"]')

    btn_login = PageElement(id_="button-submit")

    def login(self):
        """
        Clicks on the Login page
        """
        self.btn_login.click()

    def set_username(self, username: str):
        """
        Types the username in the "username" field
        """
        self.username_input.send_keys(username)

    def type_password(self, username: str):
        """
        Types the password in the "password" field
        """
        self.username_input.send_keys(username)

    def do_login(self, username: str, password: str):
        """
        Types the username, password and clicks on Login
        """
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.btn_login.click()
