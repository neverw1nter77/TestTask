import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base

class Main_page(Base):

    url = 'https://www.cian.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_rent = '//li[@class="_025a50318d--list-element--wEqv2"]'
    button_quantity_rooms = '//*[@id="frontend-mainpage"]/div/section/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[2]/button'
    button_2 = '//*[@id="frontend-mainpage"]/div/section/div/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div[2]/div/ul[1]/li[2]/button'
    button_price = '//*[@id="frontend-mainpage"]/div/section/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/button'
    input_price = '//input[@placeholder="до"]'
    input_city = '//input[@class="_025a50318d--suggestion-input--UYl_Y _025a50318d--search--rgXki _025a50318d--input--Cqvxw"]'
    button_find = '//a[@class="_025a50318d--button--ljPOU"]'

    def click_rent_button(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_rent))).click()
        print("Click on Rent button")

    def select_quantity_rooms(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_quantity_rooms))).click()
        print("Select quantity of rooms")

    def select_1_room(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_2))).click()
        print("Select 1-room apartment")

    def click_price(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_price))).click()
        print(f"Button clicked")

    def input_price_limit(self, price):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_price))).send_keys(price)
        print(f"Set price limit to {price} rubles")

    def input_city_name(self, city):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_city))).send_keys(city)
        print(f"Set city to {city}")

    def click_find_button(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_find))).click()
        print("Click on Find button")

    # Methods
    def set_filters_and_search(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(1)
        self.click_rent_button()
        self.select_quantity_rooms()
        self.select_1_room()
        self.click_price()
        self.input_price_limit('50000')
        self.input_city_name('Зеленоград')
        self.click_find_button()

