import os

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

BASE_URL = 'https://sbis.ru/'


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def wait_change_text(self, locator, text, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def wait_for_download_complete(
        self, download_dir, end_of_filename='.exe', time=30
    ):
        WebDriverWait(self.driver, time).until(
            lambda driver: any(
                filename.endswith(end_of_filename)
                for filename in os.listdir(download_dir)
            )
        )
