from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

TIMEOUT = 10  # in seconds


def get_chrome_options() -> Options:
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--incognito")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=800,600")
    opts.add_argument("--ignore-certificate-errors")
    chrome_prefs = {}
    opts.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return opts


def get_by_xpath_with_wait(browser, xpath):
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
    return WebDriverWait(browser, TIMEOUT, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
