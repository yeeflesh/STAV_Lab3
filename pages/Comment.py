import time

class Comment():
    def __init__(self, driver):
        self.driver = driver

    def writeComment(self, input):
        # click comment
        self.driver.find_element_by_xpath('//*[@id="activities"]/div[1]//*[contains(@class,"comment")]/a').click()
        time.sleep(1)

        ###
        # input comment
        # a string
        ###
        self.driver.find_element_by_xpath('//*[@id="comment-text"]').send_keys(input)
        self.driver.find_element_by_xpath('//*[@id="new_comment"]/input[2]').click()
        time.sleep(1)

        #get comment text
        commentText = self.driver.find_element_by_xpath('//*[@class="text"]/p').text

        return commentText

    def deleteComment(self):
        # get comment div id
        commentId = self.driver.find_element_by_xpath('//div[@class="comments"]/div[1]').get_attribute('id')

        # click delete comment
        #time.sleep(100)
        self.driver.find_element_by_xpath('//div[@class="comments"]//*[@class="fa fa-trash"]').click()
        time.sleep(1)

        ###
        # use try catch to prevent there is no comment(already deleted!) in the event edit mode
        # if the two commentId is not equal
        # then return true
        ###
        #time.sleep(100)
        try:
            return commentId != \
                   self.driver.find_element_by_xpath('//div[@class="comments"]/div[1]').get_attribute('id')
        except:
            return True