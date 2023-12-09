import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class ProfileEdit(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_edit_profile(self):
        driver = self.driver

        # Login
        driver.get("https://school.moodledemo.net/login/index.php")
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("moodle")
        time.sleep(2)
        driver.find_element(By.ID, "loginbtn").click()
        time.sleep(2)

        # Move to Profile
        driver.find_element(By.ID, "user-menu-toggle").click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="carousel-item-main"]/a[1]').click()
        time.sleep(2)


        driver.find_element(By.XPATH, '//*[@id="region-main"]/div/div/div[2]/section[1]/div/ul/li[1]/span/a').click()
        time.sleep(2)
        firstName = driver.find_element(By.ID, "id_firstname")
        firstName.clear()
        firstName.send_keys("Daniel")
        lastName = driver.find_element(By.ID, "id_lastname")
        lastName.clear()
        lastName.send_keys("Williams")
        # email = driver.find_element(By.ID, "id_email")
        # email.clear()
        # email.send_keys("danielwilliams912@demo.com")
        time.sleep(2)
        driver.find_element(By.ID, "id_submitbutton").click()
        time.sleep(2)
        
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()