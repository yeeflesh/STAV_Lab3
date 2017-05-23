import unittest
import time
from selenium import webdriver
from pages.Account import Account
from pages.Event import Event

class AccountTest(unittest.TestCase):

    def setUp(self):
        chromedriver = "./driver/chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.get("http://140.124.183.106:3000/")
        #self.driver.set_window_position(0, 0)
        #self.driver.set_window_size(1280, 800)
        self.driver.maximize_window()

        self.user = dict(
            email = 'coopldh@gmail.com',
            password = '88888888'
        )

    def tearDown(self):
        self.driver.close()

    def test_login(self):
        me = Account(self.driver, self.user)
        me.login()
        username = me.getUserName()

        self.assertEqual(username, '105598001')

class EventTest(unittest.TestCase):
    def setUp(self):
        chromedriver = "./driver/chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.get("http://140.124.183.106:3000/")
        #self.driver.set_window_position(0, 0)
        #self.driver.set_window_size(1280, 800)
        self.driver.maximize_window()

        self.user = dict(
            email='coopldh@gmail.com',
            password='88888888'
        )

    def tearDown(self):
        self.driver.close()

    def test_create_event(self):
        Account(self.driver, self.user).login()

        event = Event(self.driver)
        createEventData = dict(
            eventName = 'EventTest!!!',
            eventWhen = '2017/05/11 01:16'
        )
        response = event.createEvent(createEventData)

        self.assertDictEqual(response,
            dict(eventName = 'EventTest!!!',
                 eventWhen = '11 May 01:16'))


    def test_edit_event(self):
        Account(self.driver, self.user).login()

        #create event first
        event = Event(self.driver)
        createEventData = dict(
            eventName = 'EventTest!!!',
            eventWhen = '2017/05/11 01:16'
        )
        event.createEvent(createEventData)
        #time.sleep(0.5)

        #next, edit event
        editEventData = dict(
            eventName = 'EditTest???',
            eventWhen = '2017/06/13 02:37'
        )
        response = event.editEvent(editEventData)

        self.assertDictEqual(response,
            dict(eventName='EditTest???',
                 eventWhen='13 Jun 02:37'))

    def test_delete_event(self):
        Account(self.driver, self.user).login()

        #create event
        event = Event(self.driver)
        createEventData1 = dict(
            eventName='DeleteTest',
            eventWhen='2017/08/07 08:07'
        )
        event.createEvent(createEventData1)

        #delete event
        response = event.deleteEvent()

        self.assertIs(response, True)

if __name__ == "__main__":
    unittest.main()
