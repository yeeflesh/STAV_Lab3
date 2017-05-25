import unittest
import time
from selenium import webdriver
from pages.Account import Account
from pages.Event import Event
from pages.Comment import Comment
from pages.Status import Status
from pages.Friends import Friends
from pages.Profile import Profile

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
        me = Account(self.driver)
        me.login(self.user)
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
        Account(self.driver).login(self.user)

        #create event
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
        Account(self.driver).login(self.user)

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
        Account(self.driver).login(self.user)

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
        Account(self.driver).login(self.user)

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
        Account(self.driver).login(self.user)

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
        Account(self.driver).login(self.user)

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
        Account(self.driver).login(self.user)

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

class StatusTest(unittest.TestCase):
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

    def test_create_status_with_images(self):
        # login
        Account(self.driver).login(self.user)

        # create status
        status = Status(self.driver)
        createStatusData = dict(
            statusInput = 'Create Status Test!!!',
            statusImage = 'moonmoon.gif'
        )
        response = status.createStatusWithImages(createStatusData)

        self.assertEquals(response["Context"], 'Create Status Test!!!')
        self.assertIn( 'moonmoon.gif', response["ImagePath"])

    def test_edit_status(self):
        # login
        Account(self.driver).login(self.user)

        # create status
        status = Status(self.driver)
        createStatusData = dict(
            statusInput='Create Status Test!!!',
            statusImage='moonmoon.gif'
        )
        status.createStatusWithImages(createStatusData)
        time.sleep(1)

        #edit status
        editStatusData = dict(
            statusInput='Edit Status Test!!!',
            statusImage='nickyoung.gif'
        )
        response = status.editStatus(editStatusData)

        self.assertEquals(response["Context"], 'Edit Status Test!!!')
        self.assertIn('nickyoung.gif', response["ImagePath"])

    def test_delete_status(self):
        # login
        Account(self.driver).login(self.user)

        # create status
        status = Status(self.driver)
        createStatusData = dict(
            statusInput='Delete Status Test!!!',
            statusImage='nickyoung.gif'
        )
        status.createStatusWithImages(createStatusData)
        time.sleep(1)

        # delete event
        response = status.deleteStatus()

        self.assertIs(response, True)

class FriendsTest(unittest.TestCase):
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

    def test_find_friend(self):
        # login
        Account(self.driver).login(self.user)

        # find friend
        friend = Friends(self.driver)
        name = 'Red'
        response = friend.findFriends(name)

        self.assertEquals(response, 'unfollow')

class ProfileTest(unittest.TestCase):
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

    def test_edit_profile(self):
        # login
        Account(self.driver).login(self.user)

        #edit profile
        profile = Profile(self.driver)
        profileData = dict(
            avatar = 'marceline.png',
            cover = 'babyFP.png',
            name = '105598001',
            about = 'Edit Profile About',
            location = 'Edit Profile Location',
            phone = '0912345678',
            dob = '2000/08/07',
            sex = 'Male'
        )
        response = profile.editProfile(profileData)

        self.assertDictEqual(response,
            dict(
                avatarIsTheSame = True,
                coverIsTheSame = True,
                name = '105598001',
                about = 'Edit Profile About',
                location = 'Edit Profile Location',
                phone = '0912345678',
                dob = '2000/08/07',
                sex = 'Male'
            )
        )


if __name__ == "__main__":
    unittest.main()

