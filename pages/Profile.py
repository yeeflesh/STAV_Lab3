import time
import os

class Profile():
    def __init__(self, driver):
        self.driver = driver

    def editProfile(self, data):
        #click edit profile
        self.driver.find_element_by_xpath('//*[@id="links"]/h5[7]/a').click()
        time.sleep(1)

        ####
        # input data
        # avatar (image)
        # cover (image)
        # name (str)
        # about (str)
        # location (str)
        # phone (str)
        # dob (str)
        # sex (str)
        ###
        # take avatar image's direction
        avatarDir = os.path.abspath('images\\' + data['avatar'])
        self.driver.find_element_by_xpath('//*[@id="user_avatar"]').send_keys(avatarDir)
        # take cover image's direction
        coverDir = os.path.abspath('images\\' + data['cover'])
        self.driver.find_element_by_xpath('//*[@id="user_cover"]').send_keys(coverDir)
        self.driver.find_element_by_xpath('//*[@id="user_name"]').clear()
        self.driver.find_element_by_xpath('//*[@id="user_name"]').send_keys(data['name'])
        self.driver.find_element_by_xpath('//*[@id="user_about"]').clear()
        self.driver.find_element_by_xpath('//*[@id="user_about"]').send_keys(data['about'])
        self.driver.find_element_by_xpath('//*[@id="user_location"]').clear()
        self.driver.find_element_by_xpath('//*[@id="user_location"]').send_keys(data['location'])
        self.driver.find_element_by_xpath('//*[@id="user_phone_number"]').clear()
        self.driver.find_element_by_xpath('//*[@id="user_phone_number"]').send_keys(data['phone'])
        self.driver.find_element_by_xpath('//*[@id="user_dob"]').clear()
        self.driver.find_element_by_xpath('//*[@id="user_dob"]').send_keys(data['dob'])
        self.driver.find_element_by_xpath('//*[@id="user_sex"]').send_keys(data['sex'])
        self.driver.find_element_by_xpath('//*[@class="actions"]/input').click()
        time.sleep(1)

        #click edit profile
        self.driver.find_element_by_xpath('//*[@class="nav nav-pills nav-stacked"]/li[1]/a').click()
        time.sleep(1)

        #get profile data
        result = dict(
            avatarIsTheSame = True if data['avatar'] in self.driver.find_element_by_xpath('//*[@class="avatar"]').get_attribute("src") else False,
            coverIsTheSame = True if data['cover'] in self.driver.find_element_by_xpath('//*[@class="cover"]').get_attribute("style") else False,
            name = self.driver.find_element_by_xpath('//*[@id="user_name"]').get_attribute('value'),
            about = self.driver.find_element_by_xpath('//*[@id="user_about"]').get_attribute('value'),
            location = self.driver.find_element_by_xpath('//*[@id="user_location"]').get_attribute('value'),
            phone = self.driver.find_element_by_xpath('//*[@id="user_phone_number"]').get_attribute('value'),
            dob = self.driver.find_element_by_xpath('//*[@id="user_dob"]').get_attribute("value").replace('-', '/'),
            sex = self.driver.find_element_by_xpath('//*[@id="user_sex"]//*[@selected="selected"]').text
        )

        return result