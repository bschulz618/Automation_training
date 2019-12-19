import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self)
        self.driver.quit()

    def test_Challenge3(self):
        self.driver.get("https://www.copart.com/")
        self.driver.find_element(By.XPATH, //*[@id="tabTrending"]/div[1]/div[2]/div[1]/ul/li[1]/a )
        for count is elements:
            print (count.text + ": " + count.get_attribute ("href"))

    def test_Challenge3(self):
        self.driver.get("https://www.copart.com/")
        self.driver.find_element(By.XPATH, //*[@id="tabTrending"]/div[3]/div[1]/ul/li[1]/a)
        print ()

        for count is elements:
            print (elements(i).text + ": " + i.get_attribute ("href"))
            i ++ i

        print(elements[i].get_attribute("src") + ": " + elements[i].get_attributes("alt"))

        print()


if __name__ == '__main__':
    unittest.main()