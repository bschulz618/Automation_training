import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestFindaporsche(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.quit()

    def test_findaporsche(self):
        self.driver.get("https://www.copart.com/")
        self.driver.find_element(By.ID, "input-search").click()
        self.driver.find_element(By.ID, "input-search").send_keys("exotics")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-lightblue:nth-child(1)").click()
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr[1]/td[5]/span')))
        self.driver.find_element(By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr[1]/td[5]/span')
        print("done")

        print()


if __name__ == '__main__':
    unittest.main()