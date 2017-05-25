import time

class Account():
    def __init__(self, driver):
        self.driver = driver

    def login(self, userData):
        #click sign in
        self.driver.find_element_by_xpath('//*[@id="navbar-top"]/ul/li[3]/a').click()
        time.sleep(1)

        ###
        # input account
        # email
        # password
        ###
        self.driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(userData['email'])
        self.driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(userData['password'])
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()
        time.sleep(1)

    def getUserName(self):
        try:
            userName = self.driver.find_element_by_xpath('//*[@id="user-info"]/div[1]/h5/a').text
            return userName
        except:
            return 'Invalid Email or password.'