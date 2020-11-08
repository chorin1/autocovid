import os
from datetime import date

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from log_helper import set_logger
from selenium_helpers import get_chrome_options, get_by_xpath_with_wait, wait_for_xpath_to_be_stale

log = set_logger("MOE-covid")
URL = "https://parents.education.gov.il/prhnet/parents/rights-obligations-regulations/health-statement-kindergarden"
USERNAME = os.environ['MOE_USER']
PASS = os.environ['MOE_PASS']


def get_img_path():
    os.makedirs("__screenshots", exist_ok=True)
    return f"/app/__screenshots/moe{date.today().strftime('%d%m%y')}.png"


def save_screenshot(browser):
    path = get_img_path()
    log.info(f"saving screenshot {path}")
    success = browser.get_screenshot_as_file(path)
    if not success:
        return None
    return path


def wait_for_load_completion(browser):
    wait_for_xpath_to_be_stale(browser, '//*[@class="spinner-three-bounce full-screen ng-star-inserted"]')


def sign_moe():
    browser = webdriver.Chrome(options=get_chrome_options())
    try:
        browser.get(URL)

        # main page
        log.info(browser.current_url)
        button = get_by_xpath_with_wait(browser, '//input[@type="button" and @value="מילוי הצהרת בריאות מקוונת"]')
        button.click()

        # click on 'enter by username and pass' panel to enable underlying text fields
        button = get_by_xpath_with_wait(browser, '//*[@id="blocker"]')
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
        get_by_xpath_with_wait(browser,
                               '//*[@class="day-title ng-star-inserted"]')  # wait until current date is visible

        # approve all
        for button in browser.find_elements_by_xpath('//input[@type="button" and @value="מילוי הצהרת בריאות"]'):
            if not button.is_displayed():
                continue
            button.click()
            approve_btn = get_by_xpath_with_wait(browser, '//input[@value="אישור"]')
            browser.execute_script("arguments[0].click();", approve_btn)  # fixes element is not clickable error

        wait_for_load_completion(browser)
        return save_screenshot(browser)

    except TimeoutException as e:
        log.error(f"browser timed out - {e}")
    finally:
        browser.quit()
