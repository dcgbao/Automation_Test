import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class ForumPost(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_post_forum(self):
        driver = self.driver

        # Login
        driver.get("https://school.moodledemo.net/login/index.php")
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("moodle")
        driver.find_element(By.ID, "loginbtn").click()

        # self.assertIn("Python", driver.title)
        # elem = driver.find_element(By.NAME, "q")
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()