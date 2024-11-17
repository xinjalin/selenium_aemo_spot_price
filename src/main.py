import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.core.webdriver_manager import WebDriverManager
from src.core.data_extractor import DataExtractor

def main():
    url = "https://visualisations.aemo.com.au/aemo/apps/visualisation/index.html#/electricity/dashboard"
    region_id = "SA"
    periods = ["Pre-Dispatch", "Dispatch"]
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    web_driver_manager = WebDriverManager(url)
    driver = web_driver_manager.get_driver()

    try:
        extractor = DataExtractor(driver)
        extractor.select_region(region_id)

        all_data = []
        for period_id in periods:
            print(f"Selecting period: {period_id}")
            extractor.select_period(period_id)

            # Wait for summary rows to appear
            WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "summary-row"))
            )
            print("Summary rows found. Extracting data...")

            data = extractor.extract_summary_data(region_id, now, period_id)
            all_data.extend(data)

        for item in all_data:
            print(item)

    finally:
        web_driver_manager.quit()


if __name__ == "__main__":
    main()
