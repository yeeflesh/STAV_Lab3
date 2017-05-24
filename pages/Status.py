import time
import os

class Status():
    def __init__(self, driver):
        self.driver = driver

    def createStatusWithImages(self, input):
        ###
        # input status data
        # text
        # image
        ###
        self.driver.find_element_by_xpath('//*[@id="post-content"]').send_keys(input['statusInput'])
        # take image's direction
        dir = os.path.abspath('images\\' + input['statusImage'])
        # upload image
        self.driver.find_element_by_xpath('//*[@id="post_attachment"]').send_keys(dir)
        self.driver.find_element_by_xpath('//*[@id="new_post"]/div[4]/input').click()
        time.sleep(1)

        #get event data
        result = dict(
            Context = self.driver.find_element_by_xpath('//*[@id="activities"]/div[1]/div//p').text,
            ImagePath = self.driver.find_element_by_xpath('//*[@id="activities"]/div[1]//div[@class="attachment"]/img').get_attribute("src")
        )

        return result

    def editStatus(self, input):
        #click edit
        self.driver.find_element_by_xpath('//*[@id="activities"]/div[1]//*[@class="fa fa-pencil"]').click()
        time.sleep(1)

        # input status data
        # text
        # image
        ###
        self.driver.find_element_by_xpath('//*[@id="post-content"]').clear()
        self.driver.find_element_by_xpath('//*[@id="post-content"]').send_keys(input['statusInput'])
        # take image's direction
        dir = os.path.abspath('images\\' + input['statusImage'])
        # upload image
        self.driver.find_element_by_xpath('//*[@id="post_attachment"]').send_keys(dir)
        self.driver.find_element_by_xpath('//input[@value="Post"]').click()
        time.sleep(1)

        # get event data
        result = dict(
            Context=self.driver.find_element_by_xpath('//span[@class="text"]').text,
            ImagePath=self.driver.find_element_by_xpath('//div[@class="attachment"]/img').get_attribute("src")
        )

        return result

    def deleteStatus(self):
        # get status div id
        statusId = self.driver.find_element_by_xpath('//*[@id="activities"]/div[1]/div').get_attribute('id')

        # click delete event
        self.driver.find_element_by_xpath('//*[@class="fa fa-trash"]').click()
        time.sleep(1)

        ###
        # use try catch to prevent there is no post on the page
        # if the two statusId is not equal
        # then return true
        ###
        try:
            return statusId != \
                   self.driver.find_element_by_xpath('//*[@id="activities"]/div[1]/div').get_attribute('id')
        except:
            return True