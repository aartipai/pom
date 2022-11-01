from selenium.webdriver.common.by import By
from page_objects.base import Base
from selenium.common.exceptions import TimeoutException

user_management_link = (By.XPATH, "//span[contains(text(), 'User Management')]")
job_link = (By.XPATH, "//span[contains(text(), 'Job')]")

class Users(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.user_link = (By.LINK_TEXT, "Users")
        self.expand_search = (By.XPATH, "//button//i[contains(@class, 'caret-down-fill')]")
        self.search_username_txt = (By.XPATH, "//label[text()='Username']/../..//input")
        self.user_roll_ddl = (By.XPATH, "//label[text()='User Role']/../..//div[contains(@class,'select-wrapper')]")
        self.search_btn = (By.XPATH, "//button[@type='submit']")
        self.username_in_table = (By.XPATH, "//table[@id='resultTable']//a[contains(@href, 'saveSystemUser')]")

    def go_to_users_page(self):
        self.navigate_to_tab(self.admin_tab)
        self.EF.find_element(user_management_link).click()
        self.EF.find_element(self.user_link).click()

    def enter_username(self, username):
        self.EF.find_element(self.search_username_txt).clear()
        self.EF.find_element(self.search_username_txt).send_keys(username)

    def select_user_role(self, user_role):
        pass

    def enter_employee_name(self, employee_name):
        pass

    def select_status(self, status):
        pass

    def click_search_btn(self):
        self.EF.find_element(self.search_btn).click()

    def search_user(self, search_dict: dict):
        self.enter_username(search_dict.get('username', ""))
        self.select_user_role(search_dict.get('role', ""))
        self.enter_employee_name(search_dict.get('name', ""))
        self.select_status(search_dict.get('status', ""))
        self.click_search_btn()
        try:
            self.EF.find_element((By.XPATH, f"//div[text()='{search_dict.get('username')}']"))
            return True
        except TimeoutException:
            return False




#Job

class JobTitles(Base):
    def __init__(self, driver):
        self.driver = driver

class PayGrades(Base):
    def __init__(self, driver):
        self.driver = driver

class Employmentstatus(Base):
    def __init__(self, driver):
        self.driver = driver

class JobCategories(Base):
    def __init__(self, driver):
        self.driver = driver

class WorkShifts(Base):
    def __init__(self, driver):
        self.driver = driver

#Organization

class GeneralInformation(Base):
    def __init__(self, driver):
        self.driver = driver

class Locations(Base):
    def __init__(self, driver):
        self.driver = driver

class structure(Base):
    def __init__(self, driver):
        self.driver = driver

#Qualifications

class Skills(Base):
    def __init__(self, driver):
        self.driver = driver

class Education(Base):
    def __init__(self, driver):
        self.driver = driver

class Licenses(Base):
    def __init__(self, driver):
        self.driver = driver

class Languages(Base):
    def __init__(self, driver):
        self.driver = driver

class Memberships(Base):
    def __init__(self, driver):
        self.driver = driver

# Nationalities

class Nationalities (Base):
    def __init__(self, driver):
        self.driver = driver

# Corporate Branding
class CorporateBranding(Base):
    def __init__(self, driver):
        self.driver = driver

# Configuration
class EmailConfiguration(Base):
    def __init__(self, driver):
        self.driver = driver

class EmailSubscription(Base):
    def __init__(self, driver):
        self.driver = driver

class Localization(Base):
    def __init__(self, driver):
        self.driver = driver

class LanguagePackages(Base):
    def __init__(self, driver):
        self.driver = driver

class Modules(Base):
    def __init__(self, driver):
        self.driver = driver

class SocialMediaAuthentication(Base):
    def __init__(self, driver):
        self.driver = driver

class RegisterOAuthClient(Base):
    def __init__(self, driver):
        self.driver = driver



