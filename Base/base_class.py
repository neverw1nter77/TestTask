import datetime
import os

class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        print(f"Current URL: {self.driver.current_url}")


