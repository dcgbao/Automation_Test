import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class ForumPost(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_post_forum(self):
        driver = self.driver

        # Login
        driver.get("https://school.moodledemo.net/login/index.php")
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("moodle")
        time.sleep(2)
        driver.find_element(By.ID, "loginbtn").click()
        time.sleep(2)

        # Move to Forum
        # driver.find_element(By.CSS_SELECTOR, "#course-info-container-51-3 > div > div > a").click() # Locating element by CSS Selector
        driver.find_element(By.XPATH, '//*[@id="course-info-container-51-3"]/div/div/a').click() # Locating element by XPath
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="module-944"]/div/div[2]/div[1]/div/div/div/a').click()
        time.sleep(2)


        driver.find_element(By.XPATH, '//*[@id="region-main"]/div[2]/div[1]/div/div[2]/a').click()
        time.sleep(2)
        subject = driver.find_element(By.ID, "id_subject")
        subject.clear()
        subject.send_keys("Software Testing Method")

        # ------------------------------------------------------------------
        driver.switch_to.frame(driver.find_element(By.ID, "id_message_ifr"))
        message = driver.find_element(By.ID, "tinymce")
        message.clear()
        message.send_keys("What is the best software testing method?")
        driver.switch_to.default_content()  # Switch back to the main content
        # ------------------------------------------------------------------

        time.sleep(2)
        # driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/div[2]/div/section/div[2]/div[2]/div[2]/form/div[4]/div[2]/fieldset/div/div[1]/span/input').click() # Locating element by full XPath
        driver.find_element(By.ID, "id_submitbutton").click() # Locating element by ID
        time.sleep(2)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()