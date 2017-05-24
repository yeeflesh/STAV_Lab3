import unittest
import time
from selenium import webdriver
from pages.Account import Account
from pages.Event import Event
from pages.Comment import Comment

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
        # login
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
        # login
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
        # login
        Account(self.driver, self.user).login()

        #create event first
        event = Event(self.driver)
        createEventData = dict(
            eventName = 'EventTest!!!',
            eventWhen = '2017/05/11 01:16'
        )
        event.createEvent(createEventData)
        time.sleep(1)

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
        #login
        Account(self.driver, self.user).login()

        #create event
        event = Event(self.driver)
        createEventData = dict(
            eventName='DeleteTest',
            eventWhen='2017/08/07 08:07'
        )
        event.createEvent(createEventData)
        time.sleep(1)

        #delete event
        response = event.deleteEvent()

        self.assertIs(response, True)

    def test_like_event(self):
        # login
        Account(self.driver, self.user).login()

        # create event
        event = Event(self.driver)
        createEventData = dict(
            eventName='LikeTest',
            eventWhen='2017/08/07 08:07'
        )
        event.createEvent(createEventData)
        time.sleep(1)

        # like event
        response = event.likeEvent()

        self.assertEquals(response, 'unlike')

    def test_unlike_event(self):
        # login
        Account(self.driver, self.user).login()

        # create event
        event = Event(self.driver)
        createEventData = dict(
            eventName='UnlikeTest',
            eventWhen='2017/08/07 08:07'
        )
        event.createEvent(createEventData)
        time.sleep(1)

        # unlike event
        response = event.unlikeEvent()

        self.assertEquals(response, 'like')

class CommentTest(unittest.TestCase):
    def setUp(self):
        chromedriver = "./driver/chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.get("http://140.124.183.106:3000/")
        # self.driver.set_window_position(0, 0)
        # self.driver.set_window_size(1280, 800)
        self.driver.maximize_window()

        self.user = dict(
            email='coopldh@gmail.com',
            password='88888888'
        )

    def tearDown(self):
        self.driver.close()

    def test_write_comment(self):
        # login
        Account(self.driver, self.user).login()

        #create event first
        createEventData = dict(
            eventName='Create A Event For WriteCommentTest',
            eventWhen='2017/08/07 08:07'
        )
        Event(self.driver).createEvent(createEventData)

        #write a comment
        comment = Comment(self.driver)
        text = 'Write Comment Test!!!'
        response = comment.writeComment(text)

        self.assertEqual(response, 'Write Comment Test!!!')

    def test_delete_comment(self):
        # login
        Account(self.driver, self.user).login()

        # create event first
        createEventData = dict(
            eventName='Create A Event For DeleteCommentTest',
            eventWhen='2017/08/07 08:07'
        )
        Event(self.driver).createEvent(createEventData)

        # write a comment first
        comment = Comment(self.driver)
        text = 'Delete Comment Test!!!'
        comment.writeComment(text)
        time.sleep(1)

        #delete comment
        response = comment.deleteComment()

        self.assertIs(response, True)

if __name__ == "__main__":
    unittest.main()
