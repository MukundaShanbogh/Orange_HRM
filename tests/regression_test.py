from pages.login_page import Login


class Test_Regression:

    def test_invalid_login(self, pages):
        lgn = Login(pages)
        lgn.invalid_login()
        lgn.empty_credentials()
        lgn.valid_login()
        lgn.logout()