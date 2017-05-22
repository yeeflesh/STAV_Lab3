import unittest
import json
from selenium import webdriver
from pages.Account import Account
from pages.Event import Event

class WebApplicationTest(unittest.TestCase):

    def setUp(self):
        chromedriver = "./driver/chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.get("http://140.124.183.106:3000/")
        #self.driver.set_window_position(0, 0)
        #self.driver.set_window_size(1280, 800)
        self.driver.maximize_window()

        self.user = {
            'email': 'coopldh@gmail.com',
            'password': '88888888'
        }

    def tearDown(self):
        self.driver.close()

    def test_login(self):
        me = Account(self.driver, json.dumps(self.user))
        me.login()
        username = me.getUserName()

        assert username, '105598001'

    def test_create_event(self):
        Account(self.driver, json.dumps(self.user)).login()

        createEventData = {
            'eventName' : 'EventTest!!!',
            'eventWhen' : '2017/05/11 01:16'
        }
        event = Event(self.driver)
        response = json.loads(event.createEvent(json.dumps(createEventData)))

        assert response, \
            {'eventName': 'EventTest!!!',
            'eventWhen': '11 May 01:16'}

if __name__ == "__main__":
    unittest.main()
