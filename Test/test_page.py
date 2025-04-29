from Pages.main_page import Main_page
from Pages.negative_page import Second_page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_happy_path():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start test 1")

    positive_test = Main_page(driver)
    positive_test.fill_form_happy_path()

    negative_test = Second_page(driver)
    negative_test.fill_form_negative_path()



