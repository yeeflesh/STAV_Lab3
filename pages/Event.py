import time

class Event():
    def __init__(self, driver):
        self.driver = driver

    def createEvent(self, input):
        #click create event
        self.driver.find_element_by_xpath('//*[@id="links"]/h5[2]/a').click()
        time.sleep(0.5)

        ###
        # input event data
        # name
        # when
        ###
        self.driver.find_element_by_xpath('//*[@id="event_name"]').send_keys(input['eventName'])
        self.driver.find_element_by_xpath('//*[@id="event_event_datetime"]').send_keys(input['eventWhen'])
        self.driver.find_element_by_xpath('//*[@id="new_event"]/div[3]/input').click()
        time.sleep(0.5)

        #get event data
        result = dict(
            eventName=self.driver.find_element_by_xpath('//*[@id="activities"]/div[1]/div//h3').text,
            eventWhen=self.driver.find_element_by_xpath('//*[@id="activities"]/div[1]/div//div[@class="content"]/span').text
        )

        return result

    def editEvent(self, input):
        # click eidt event
        self.driver.find_element_by_xpath('//*[@class="btn btn-primary btn-sm"]').click()
        time.sleep(0.5)

        ###
        # input event data
        # name
        # when
        ###
        self.driver.find_element_by_xpath('//*[@id="event_name"]').clear()
        self.driver.find_element_by_xpath('//*[@id="event_name"]').send_keys(input['eventName'])
        self.driver.find_element_by_xpath('//*[@id="event_event_datetime"]').clear()
        self.driver.find_element_by_xpath('//*[@id="event_event_datetime"]').send_keys(input['eventWhen'])
        self.driver.find_element_by_xpath('//*[@value="update"]').submit()
        time.sleep(0.5)

        # get event data
        result = dict(
            eventName = self.driver.find_element_by_xpath('//*[@class="content"]/h3').text,
            eventWhen = self.driver.find_element_by_xpath('//*[@class="content"]/span').text
        )

        return result

    def deleteEvent(self):
        #get event div id
        eventId = self.driver.find_element_by_xpath('//*[@id="activities"]/div[1]/div').get_attribute('id')

        # click delete event
        self.driver.find_element_by_xpath('//*[@class="fa fa-trash"]').click()
        time.sleep(0.5)

        ###
        # use try catch to prevent there is no post on the page
        # if the two eventId is not equal
        # then return true
        ###
        try:
            return eventId != \
                self.driver.find_element_by_xpath('//*[@id="activities"]/div[1]/div').get_attribute('id')
        except:
            return True