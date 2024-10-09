import os
import time

from sbis_pages import PhotoChecker, RegionChanger, FileDownloader


def test_tensor_photos(browser):
    driver = PhotoChecker(browser)
    driver.go_to_site()
    driver.go_to_contacts()
    driver.click_on_tensor()
    browser.switch_to.window(browser.window_handles[1])
    assert driver.find_title_power_in_people().text == 'Сила в людях'
    driver.click_about()
    assert browser.current_url == 'https://tensor.ru/about'
    photo_sizes = driver.find_work_photos()
    assert all(
        photo_size == photo_sizes[0] for photo_size in photo_sizes
    ) == True


def test_change_region(browser):
    driver = RegionChanger(browser)
    driver.go_to_site()
    driver.go_to_contacts()
    region = driver.get_region()
    # assert region == 'Архангельская обл.'
    partners_old_region = driver.get_partners()
    driver.change_region()
    region = driver.get_region()
    assert region == 'Камчатский край'
    partners_new_region = driver.get_partners()
    assert partners_old_region != partners_new_region
    assert browser.current_url.split(
        '/'
    )[4].split('?')[0] == '41-kamchatskij-kraj'
    assert browser.title.split('—')[1].strip() == 'Камчатский край'


def test_download_file(browser):
    driver = FileDownloader(browser)
    driver.go_to_site()
    file_size = float(driver.download_file().split(' ')[2])
    driver.wait_for_download_complete(os.getcwd())
    assert any(
        filename.endswith('.exe') for filename in os.listdir(os.getcwd())
    )
    assert (
       round(
           (os.path.getsize(
               os.path.join(os.getcwd(), 'sbisplugin-setup-web.exe')
           ) / (1024 * 1024)),
           2
       )
    ) == file_size
