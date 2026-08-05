import pytest

from pages.login_page import Login
from utils.data_reader import read_csv_data


class Test_Regression:

    @pytest.mark.parametrize("username, password", read_csv_data("test_data/user_name.csv"))
    def test_invalid_login(self, pages, username, password):
        lgn = Login(pages)
        lgn.invalid_login(username, password)

    def test_empty_credentials(self, pages):
        lgn = Login(pages)
        lgn.empty_credentials()

    def test_valid_login(self, pages):
        lgn = Login(pages)
        lgn.valid_login()

    def test_logout(self, pages):
        lgn = Login(pages)
        lgn.valid_login()
        lgn.logout()
        