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