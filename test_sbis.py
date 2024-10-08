from sbis_pages import PhotoChecker


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