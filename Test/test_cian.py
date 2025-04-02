import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from Pages.main_page import Main_page
from Pages.filter_page import Filter_page


def test_cian():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start test")

    main_page = Main_page(driver)
    main_page.set_filters_and_search()
    time.sleep(4)

    filter_page = Filter_page(driver)
    filter_page.features()

    print("Test Finished")




