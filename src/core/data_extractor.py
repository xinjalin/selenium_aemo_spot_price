from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from src.core.data_item import DataItem


class DataExtractor:
    def __init__(self, driver):
        self.driver = driver

    def select_region(self, region_id):
        dropdown = Select(WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "region-id"))
        ))
        dropdown.select_by_visible_text(region_id)

    def select_period(self, period_id):
        dropdown = Select(WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "period"))
        ))
        dropdown.select_by_visible_text(period_id)

    def extract_summary_data(self, region_id, time, period_id):
        data_items = []
        summary_rows = self.driver.find_elements(By.CLASS_NAME, "summary-row")

        for row in summary_rows:
            title = row.find_element(
                By.CLASS_NAME, "summary-row-label-title").text
            unit = row.find_element(
                By.CLASS_NAME, "summary-row-label-unit").text.strip('()')
            value = row.find_element(By.CLASS_NAME, "summary-row-value").text

            data_items.append(DataItem(name=title, unit=unit, value=value,
                                       region=region_id, time=time, period=period_id))
        return data_items
