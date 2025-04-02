import datetime
import os

class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        print(f"Current URL: {self.driver.current_url}")

    def get_screenshot(self):
        timestamp = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        screenshot_name = f"screenshot_{timestamp}.png"
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'page')

        if not os.path.exists(desktop_path):
            os.makedirs(desktop_path)

        screenshot_path = os.path.join(desktop_path, screenshot_name)
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved as {screenshot_path}.")
