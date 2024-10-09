from base_app import BasePage
from selenium.webdriver.common.by import By


class SbisLocators:
    CONTACTS = (By.CLASS_NAME, 'sbisru-Header-ContactsMenu')
    MORE_OFFICES = (By.CLASS_NAME, 'sbisru-Header-ContactsMenu__arrow-icon')
    TENSOR_BANNER = (By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')
    REGION = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
    PARTNERS = (By.CLASS_NAME, 'sbisru-Contacts-List__name')
    KAMCHATKA = (By.CSS_SELECTOR, 'span[title="Камчатский край"]')
    DOWNLOAD = (By.CSS_SELECTOR, '.sbisru-Footer__link[href="/download"]')
    SBIS_PLUGIN = (
        By.XPATH,
        '//div[@class="controls-TabButton__caption" and text()="СБИС Плагин"]'
    )
    WINDOWS = (By.XPATH, '//span[text()="Windows"]')
    DOWNLOAD_BUTTON = (By.CLASS_NAME, 'sbis_ru-DownloadNew-loadLink__link')


class TensorLocators:
    POWER_IN_PEOPLE = (By.CLASS_NAME, 'tensor_ru-Index__block4-content')
    POWER_IN_PEOPLE_TITLE = (By.CLASS_NAME, 'tensor_ru-Index__card-title')
    POWER_IN_PEOPLE_ABOUT = (By.CLASS_NAME, 'tensor_ru-link')
    WORK_PHOTOS = (
        By.CSS_SELECTOR, '.tensor_ru-About__block3-image-wrapper img'
    )


class SbisContacts(BasePage):
    def go_to_contacts(self):
        self.find_element(SbisLocators.CONTACTS, time=2).click()
        return self.find_element(SbisLocators.MORE_OFFICES, time=5).click()


class PhotoChecker(SbisContacts):
    def click_on_tensor(self):
        return self.find_element(SbisLocators.TENSOR_BANNER,time=2).click()

    def find_block_power_in_people(self):
        return self.find_element(TensorLocators.POWER_IN_PEOPLE, time=2)

    def find_title_power_in_people(self):
        return self.find_block_power_in_people().find_element(
            *TensorLocators.POWER_IN_PEOPLE_TITLE
        )

    def click_about(self):
        return self.find_block_power_in_people().find_element(
            *TensorLocators.POWER_IN_PEOPLE_ABOUT
        ).click()

    def find_work_photos(self):
        photos = self.find_elements(TensorLocators.WORK_PHOTOS, time=2)
        return [
            (photo.get_attribute('width'), photo.get_attribute('height'))
            for photo in photos
        ]


class RegionChanger(SbisContacts):
    def find_region(self):
        return self.find_element(SbisLocators.REGION, time=2)

    def get_region(self):
        return self.find_region().text

    def get_partners(self):
        partners = self.find_elements(SbisLocators.PARTNERS, time=2)
        return [partner.text for partner in partners]

    def change_region(self):
        self.find_region().click()
        self.find_element(SbisLocators.KAMCHATKA, time=10).click()
        return self.wait_change_text(
            SbisLocators.REGION, text='Камчатский край'
        )


class FileDownloader(BasePage):
    def download_file(self):
        self.find_element(SbisLocators.DOWNLOAD, time=2).click()
        self.find_element(SbisLocators.SBIS_PLUGIN, time=2).click()
        self.find_element(SbisLocators.WINDOWS, time=2).click()
        download_button = self.find_elements(SbisLocators.DOWNLOAD_BUTTON, time=2)[0]
        download_button.click()
        return download_button.text
