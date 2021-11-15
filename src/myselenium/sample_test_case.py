from enum import Enum
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import selenium.common.exceptions as exceptions
from util.selenium_util import SeleniumUtil as su
from util.config import Config
from util.file_control import FileControl as fctrl

class TestCase:
    
    def __init__(self):
        self._root_url = Config.get_pages()["root"]
        self._user_signin_id = Config.get_signin_id()
        self._user_signin_password = Config.get_signin_password()
        self._driver = su.get_driver()
        self._web_driver_wait = WebDriverWait(self._driver, 20)


    def open_page(self, url):
        self._driver.get(url)
        self._web_driver_wait.until(EC.presence_of_element_located((By.TAG_NAME, "meta"))) # wait till the page is loaded


    def get_source(self):
        return self._driver.page_source

    def sign_in(self):
        # Access to the sign in page
        signin_url = Config.get_pages_for_signup_flow_test()["signin"]
        self._driver.get(signin_url)
        
        # Put the signin id in the form
        signin_id_element = WebDriverWait(self._driver, 15).until(EC.presence_of_element_located((By.ID, 'signinid')))
        #signin_id_element = self._web_driver_wait.until(EC.presence_of_element_located((By.ID, "signinid")))
        signin_id_element.clear()
        signin_id_element.send_keys(self._user_signin_id)

        # Put the passwoed in the form
        password_element = self._driver.find_element_by_id("password")
        password_element.clear()
        password_element.send_keys(self._user_signin_password)

        # Click the signin button
        self._driver.find_element_by_id("login").click()


    def go_to_checkout(self):
        checkout_btn = self._web_driver_wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Checkout")))
        checkout_btn.click()

    def proceed_to_checkout(self, completes_checkout=False):
        # Select a size
        size_select_ele = Select(self._driver.find_element_by_id("size"))
        size_select_ele.select_by_value("large")

        # Complete the checkout
        if completes_checkout:
            checkout_btn = self._web_driver_wait.until(EC.element_to_be_clickable((By.ID,"checkout")))
            checkout_btn.click()


    def check_if_the_page_is_properly_displayed(self, page):
        try: 
            self._driver.get(page)
            self._web_driver_wait.until(EC.presence_of_element_located((By.TAG_NAME,"meta")))

        except exceptions.TimeoutException:
            print(f"TimeoutException occurs in {page}")
            return False

        page_source = self._driver.page_source

        # Sign in again if signed out
        signin_page_pattern = r"(?:<title>)[\s\S]*Sign in[\s\S]*(?:<\/title>)"
        compiled_signin_page_pattern = re.compile(signin_page_pattern)
        is_signin_page = fctrl.contains(page_source, compiled_pattern=compiled_signin_page_pattern)
        if is_signin_page:
            print("sign in again")
            self.sign_in()
            result = self.check_if_the_page_is_properly_displayed(page)
            return result 

        # Check if the page is an error page
        error_page_patterns = [ r"(?:Description:)[\s\S]*(?:Exception Details:)[\s\S]*(?:Source Error:)", r"(?:<title>)[\s\S]*Error Page[\s\S]*(?:<\/title>)" ]
        is_error_page = fctrl.find_with_multiple_regex_patterns(page_source, error_page_patterns)
        return (is_error_page == False)
        