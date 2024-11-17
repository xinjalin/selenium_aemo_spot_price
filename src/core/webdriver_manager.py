from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebDriverManager:
    def __init__(self, url):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)
        self.url = url

    def get_driver(self):
        self.driver.get(self.url)
        return self.driver

    def quit(self):
        self.driver.quit()
