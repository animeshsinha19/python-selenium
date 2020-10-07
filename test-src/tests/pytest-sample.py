import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='../../chromedriver')
        self.wait = WebDriverWait(self.driver, 5)
        self.action_chains = ActionChains(self.driver)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.daily-harvest.com/")
        driver.maximize_window()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.primary-nav > .dropdown')))
        dropdown_icon = driver.find_element_by_css_selector('.primary-nav > .dropdown')
        print dropdown_icon

        self.action_chains.move_to_element(dropdown_icon)
        self.action_chains.click(dropdown_icon)
        self.action_chains.perform()

        dropdown_icon.click()
        self.action_chains.pause(5)
        self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.dropdown-menu.show > div > a')))
        menu_items = driver.find_elements_by_css_selector('.dropdown-menu.show > div > a')
        for item in menu_items:
            print item.text

    def test_test(self):
        # from Selenium IDE
        self.driver.get("https://www.daily-harvest.com/")
        self.driver.set_window_size(1920, 981)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.primary-nav > .dropdown')))
        self.driver.find_element(By.CSS_SELECTOR, ".has-caret").click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div:nth-child(1) > .pl-8:nth-child(2) > span')))
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .pl-8:nth-child(2) > span").click()
        self.driver.find_element(By.ID, "TZWbOshkeag3").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.find_element(By.ID, "postalCode").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-link").click()
        self.driver.find_element(By.ID, "postalCode").click()
        self.driver.find_element(By.ID, "postalCode").send_keys("12345")
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("1234@test.com")
        self.driver.find_element(By.CSS_SELECTOR, ".welcome-step-cta-wrap > .w-100").click()
        self.driver.find_element(By.CSS_SELECTOR, ".w-100:nth-child(1) .custom-control-label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".button").click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
