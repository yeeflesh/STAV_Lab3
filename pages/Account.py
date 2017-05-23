import time

class Account():
    def __init__(self, driver, userData):
        self.driver = driver
        self.userData = userData

    def login(self):
        #click sign in
        self.driver.find_element_by_xpath('//*[@id="navbar-top"]/ul/li[3]/a').click()
        time.sleep(0.5)

        ###
        # input account
        # email
        # password
        ###
        self.driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(self.userData['email'])
        self.driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(self.userData['password'])
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()
        time.sleep(0.5)

    def getUserName(self):
        return self.driver.find_element_by_xpath('//*[@id="user-info"]/div[1]/h5/a').text