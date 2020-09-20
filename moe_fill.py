import os
from datetime import date

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from log_helper import set_logger
from selenium_helpers import get_chrome_options, get_by_xpath_with_wait

log = set_logger("MOE-covid")
URL = "https://parents.education.gov.il/prhnet/parents/rights-obligations-regulations/health-statement-kindergarden"
USERNAME = os.environ['MOE_USER']
PASS = os.environ['MOE_PASS']


def get_todays_date():
    return date.today().strftime("%d%m%y")


def sign_moe():
    browser = webdriver.Chrome(options=get_chrome_options())
    try:
        browser.get(URL)

        # main page
        log.info(browser.current_url)
        button = get_by_xpath_with_wait(browser, '//input[@type="button" and @value="מילוי הצהרת בריאות מקוונת"]')
        button.click()

        # enter username and password page
        log.info(browser.current_url)
        username_path = '//*[@id="HIN_USERID"]'
        password_path = '//*[@id="Ecom_Password"]'
        submit_btn = '//*[@id="loginButton2"]'

        button = get_by_xpath_with_wait(browser, submit_btn)
        browser.find_element_by_xpath(username_path).send_keys(USERNAME)
        browser.find_element_by_xpath(password_path).send_keys(PASS)
        button.click()

        # fill form page
        log.info(browser.current_url)
        get_by_xpath_with_wait(browser, '//*[@class="day-title"]')  # wait until current date is visible

        for button in browser.find_elements_by_xpath('//input[@type="button" and @value="מילוי הצהרת בריאות"]'):
            button.click()
            approve_btn = get_by_xpath_with_wait(browser, "//input[@value='אישור']")
            approve_btn.click()

        # wait for at least one checkmark
        get_by_xpath_with_wait(browser, '//*[@class="fa fa-check-circle"]')

        return browser.get_screenshot_as_png()

    except TimeoutException as e:
        log.critical("browser timed out - ", e)
    finally:
        browser.quit()
