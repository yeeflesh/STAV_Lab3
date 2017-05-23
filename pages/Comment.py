import time

class Comment():
    def __init__(self, driver):
        self.driver = driver

    def writeComment(self, input):
        # click comment
        self.driver.find_element_by_xpath('//*[@id="activities"]/div[1]//*[contains(@class,"comment")]/a').click()
        time.sleep(0.5)

        ###
        # input comment
        # a string
        ###
        self.driver.find_element_by_xpath('//*[@id="comment-text"]').send_keys(input)
        self.driver.find_element_by_xpath('//*[@id="new_comment"]/input[2]').click()
        time.sleep(0.5)

        #get comment text
        commentText = self.driver.find_element_by_xpath('//*[@class="text"]/p').text

        return commentText