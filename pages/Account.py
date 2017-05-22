import time
import json

class Account():
    def __init__(self, driver, jsonObj):
        self.driver = driver
        self.jsonObj = json.loads(jsonObj)

    def login(self):
        #click sign in
        self.driver.find_element_by_xpath('//*[@id="navbar-top"]/ul/li[3]/a').click()

        ###
        # input account
        # email
        # password
        ###
        self.driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(self.jsonObj['email'])
        self.driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(self.jsonObj['password'])
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()
        time.sleep(0.5)

    def getUserName(self):
        return self.driver.find_element_by_xpath('//*[@id="user-info"]/div[1]/h5/a').text