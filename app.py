 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class dss_bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('http://dss.nitc.ac.in/nitcreg/RegLogin.aspx')
        email = bot.find_element_by_id('txtuname')
        password = bot.find_element_by_id('txtpassword')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

    def do_stuff(self):
        bot = self.bot
        bot.get('http://dss.nitc.ac.in/nitcreg/tlogin.aspx')
        selects = bot.find_elements_by_id('ddlcourse')
        for select in selects:
            options = [x for x in select.find_elements_by_tag_name("option")]
        print(len(options))
        while(len(options) > 0):
            bot.find_element_by_id('Button3').click()
            alert = bot.switch_to.alert
            alert.accept()
            # select_box = bot.find_element_by_id('ddlteacher')
            # options = [x for x in select_box.find_elements_by_tag_name("option")]
            # for element in options:
            #     print (element.text)
            bot.find_element_by_id('Button1').click()
            selects = bot.find_elements_by_tag_name('select')
            for select in selects:
                options = [x for x in select.find_elements_by_tag_name("option")]
                for option in options:
                    # print(option.text)
                    if (option.text == 'Good'):
                        option.click()
                    #     print("selected Good")
                    elif(option.text == '90'):
                        option.click()
                    elif(option.text == 'Yes'):
                        option.click() 
                    #     print("selected 90")
                    # break
            bot.find_element_by_id('Button1').click()

        alert = bot.switch_to.alert
        alert.accept()



x = dss_bot('B170373EE', 'B170373EE') 
x.login()
x.do_stuff()
