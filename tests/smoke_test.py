from pages.login_page import Login


class Test_smoke:
    def test_login(self,pages):
        lgn = Login(pages)
        lgn.valid_login()