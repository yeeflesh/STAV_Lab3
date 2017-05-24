import time

class Friends():
    def __init__(self, driver):
        self.driver = driver

    def findFriends(self, targetName):
        #click friends first
        self.driver.find_element_by_xpath('//*[@id="links"]/h5[4]/a').click()
        time.sleep(1)

        # find target name in friends and unfollow him/her
        self.findFriendAndFollow(targetName)

        #click find Friends
        self.driver.find_element_by_xpath('//*[@id="links"]/h5[6]/a').click()
        time.sleep(1)

        # find target name in find friends and follow him/her
        return self.findFriendAndFollow(targetName)


    def checkFriendExsist(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
            return True
        except:
            return False

    ###
    # find target name in friends
    # if already follow
    # then
    # unfollow
    ###
    def findFriendAndFollow(self, name):
        friendNameXpath = '//*[contains(text(), "' + name + '")]'
        friendFollowButtonXpath = friendNameXpath + '/../../..//button'

        if self.checkFriendExsist(friendNameXpath) :
            self.driver.find_element_by_xpath(friendFollowButtonXpath).click()
            time.sleep(1)

            return self.driver.find_element_by_xpath(friendFollowButtonXpath).text
        else:
            return 'No Friends found.'