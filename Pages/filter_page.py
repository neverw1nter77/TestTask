import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base


class Filter_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def go_to_page_10(self):
        try:
            current_url = self.driver.current_url
            if "&p=" in current_url:
                new_url = current_url.replace(f"&p={current_url.split('&p=')[1].split('&')[0]}", "&p=10")
            else:
                new_url = current_url + "&p=10"

            self.driver.get(new_url)
            print(f"Перешел на страницу 10: {new_url}")
        except Exception as e:
            print(f"Ошибка при переходе на страницу 10: {e}")


    def select_10th_apartment(self):
        try:
            apartments = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//article[contains(@data-name, "CardComponent")]'))
            )
            if len(apartments) >= 10:
                apartments[9].click()
                print("Открыта 10-я квартира")
                self.driver.switch_to.window(self.driver.window_handles[-1])
            else:
                print("Не найдено 10 квартир.")
        except Exception as e:
            print(f"Ошибка при выборе 10-й квартиры: {e}")


    def scroll_down(self):
        try:
            self.driver.execute_script("window.scrollBy(0, 3100);")
            print("Прокрутили страницу вниз на 3100px")
        except Exception as e:
            print(f"Ошибка при прокрутке страницы: {e}")

    def features(self):
        self.go_to_page_10()
        time.sleep(3)
        self.select_10th_apartment()
        time.sleep(3)
        self.scroll_down()
        time.sleep(5)
        self.get_screenshot()


