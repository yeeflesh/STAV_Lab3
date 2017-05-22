import time
import json

class Event():
    def __init__(self, driver):
        self.driver = driver

    def createEvent(self, inputJson):
        data = json.loads(inputJson)

        #clidk create event
        self.driver.find_element_by_xpath('//*[@id="links"]/h5[2]/a').click()

        ###
        # input event data
        # name
        # when
        ###
        self.driver.find_element_by_xpath('//*[@id="event_name"]').send_keys(data['eventName'])
        self.driver.find_element_by_xpath('//*[@id="event_event_datetime"]').send_keys(data['eventWhen'])
        self.driver.find_element_by_xpath('//*[@id="new_event"]/div[3]/input').click()
        time.sleep(0.5)

        #get event data
        result = {
            'eventName' : self.driver.find_element_by_xpath('//*[@id="event-1146"]/div[2]/h3').text,
            'eventWhen' : self.driver.find_element_by_xpath('//*[@id="event-1146"]/div[2]/span').text
        }

        return json.dumps(result)