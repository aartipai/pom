from_page_objects.login import Login
from page_objects.admin import users
from utility.create_webdriver import webdriver
import pytest

USERS = [[{"username": "Alice.Duval"}, True], [{"username": "Kapil"}, False]]
@pytest.fixture()
def setup():
     driver = webdriver()
     login_obj = Login(driver)
     user_obj = users(driver)
     Login_obj.Login()
     yield Login_obj,user_obj
     user_obj.logout()


@pytest.ark.parametrize("search_dict,present",users)
def test_search_user(setup,search_dict,present):
     Login_obj,user_obj = setup
     user_obj.navigate_to_tab(user_obj.admin_tab)
     user_obj_go_to_user_page()
     assert user_obj.serach_user(serach_dict) ==present




