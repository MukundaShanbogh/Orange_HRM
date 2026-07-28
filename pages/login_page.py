from playwright.sync_api import expect
from config.config import Config


class Login_locators:
    user_name = "Username"
    password ="Password"
    login = " Login "
    forgot_password_btn = "Forgot your password? "
    invalid_credentials_txt = "Invalid credentials"
    required = "Required"
    profile_name = "//span//p"
    logout = "Logout"

class Login:
    def __init__(self,pages):
        self.pages = pages

    def valid_login(self):
        ll = Login_locators()
        user_name=self.pages.get_by_placeholder(ll.user_name)
        user_name.fill(Config.user_name)
        password =  self.pages.get_by_placeholder(ll.password)
        password.fill(Config.password)
        login_btn = self.pages.get_by_role("button",name=ll.login)
        login_btn.click()
        expect(self.pages).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")


    def invalid_login(self,username,password):
        ll = Login_locators()
        user_name = self.pages.get_by_placeholder(ll.user_name)
        user_name.fill(username)
        password_locator = self.pages.get_by_placeholder(ll.password)
        password_locator.fill(password)
        login_btn = self.pages.get_by_role("button", name=ll.login)
        login_btn.click()
        expect(self.pages.get_by_text(ll.invalid_credentials_txt)).to_have_text("Invalid credentials")


    def empty_credentials(self):
        ll = Login_locators()
        user_name = self.pages.get_by_placeholder(ll.user_name)
        user_name.fill("")
        password = self.pages.get_by_placeholder(ll.password)
        password.fill("")
        login_btn = self.pages.get_by_role("button", name=ll.login)
        login_btn.click()
        expect(self.pages.get_by_text(ll.required).first).to_be_visible()

    def logout(self):
        ll = Login_locators()
        profile_name = self.pages.locator(ll.profile_name)
        profile_name.click()
        logout = self.pages.get_by_text(ll.logout)
        logout.click()
