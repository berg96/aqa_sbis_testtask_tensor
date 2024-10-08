from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = 'https://sbis.ru/'


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver,time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver,time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    def wait_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator)
        )

    def go_to_site(self):
        return self.driver.get(self.base_url)