import unittest
import functions as f
import xpath
from selenium import webdriver

expected_url = xpath.exp_url()


class TestBookingRoomFunctionality(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.phptravels.net/signup')

    def test_booking(self):
        final_page_url = f.actions()
        self.driver.implicitly_wait(15)
        assert final_page_url == expected_url

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
