import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base
from selenium.webdriver.support.ui import Select


class Second_page(Base):


    url = 'https://qatest.datasub.com/quote.html'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    name_field = '//input[@id="q_name"]'
    email_field = '//input[@id="q_email"]'
    service_dropdown = '//select[@id="q_service"]'
    message_field = '//textarea[@id="q_message"]'
    submit_button = '//button[@class="btn btn-dark w-100 py-3"]'


    def fill_name(self, name):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_field))).send_keys(name)
        print(f"Entered name: {name}")

    def fill_email(self, email):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_field))).send_keys(email)
        print(f"Entered email: {email}")

    def select_service(self):
        dropdown_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.service_dropdown))
        )
        select = Select(dropdown_element)
        select.select_by_visible_text("Service 1")
        print(f"Selected service: Service 1")


    def fill_message(self, message):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.message_field))).send_keys(message)
        print(f"Entered message: {message}")

    def click_button(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submit_button))).click()
        print("Clicked Submit")




    # Negative path
    def fill_form_negative_path(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)
        self.fill_name("Alex Petrov")
        time.sleep(1)
        self.fill_email("alex@example.commmm")
        time.sleep(1)
        self.select_service()
        self.fill_message("Random message")
        time.sleep(1)
        self.click_button()
