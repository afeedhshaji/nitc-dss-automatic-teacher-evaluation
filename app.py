from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys


class dss_bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def not_a_number(grade):
        if grade not in [1,2,3,4,5]:
            grade = int(input("Enter only one number from 1 to 5: "))
            grade = not_a_number(grade)
        else: return grade
    
    def login(self):
        bot = self.bot
        bot.get('http://dss.nitc.ac.in/nitcreg/RegLogin.aspx')
        email = bot.find_element(By.ID, 'txtuname')
        password = bot.find_element(By.ID, 'txtpassword')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

    def do_stuff(self):
        bot = self.bot
        bot.get('http://dss.nitc.ac.in/nitcreg/tlogin.aspx')
        html= bot.find_element(By.XPATH, ".//html")

        if ('completed' in html.text):
            print("You've already completed the teacher evaluation")
            time.sleep(5)
            bot.quit()
            sys.exit()
            
        selects = bot.find_elements(By.ID, 'ddlcourse')
        for select in selects:
            options = [x for x in select.find_elements(By.TAG_NAME,"option")]
        print("Total number of subjects:",len(options),end="\n")
        print("Type number: \n1 for Excellent\n2 for very good\n3 for good\n4 for fair\n5 for poor\n")
        while(len(options) > 0):
            try:
                bot.find_element(By.ID,'Button3').click()
                alert = bot.switch_to.alert
                alert.accept()
                select_box = bot.find_element(By.ID,'ddlteacher')
                options = [x for x in select_box.find_elements(By.TAG_NAME,"option")]
                for element in options:
                    print ("\nTeacher name:",element.text)
                    grade = int(input("Enter rating: "))
                    if(grade not in [1,2,3,4,5]):
                        grade = not_a_number(grade) 
                    rating = {1:'Excellent',2:'Very Good',3:'Good',4:'Fair',5:'Poor'}
                bot.find_element(By.ID,'Button1').click()
                selects = bot.find_elements(By.TAG_NAME,'select')
                for select in selects:
                    options = [x for x in select.find_elements(By.TAG_NAME,"option")]
                    for option in options:
                        if (option.text == rating[grade]):
                            option.click()
                        elif(option.text == '90'):
                            option.click()
                        elif(option.text == 'Yes'):
                            option.click() 
                bot.find_element(By.ID,'Button1').click()
            except:
                print("\nEvaluation Complete.")
                time.sleep(5)
                bot.quit()
                break

x = dss_bot(sys.argv[1], sys.argv[2]) 
x.login()
x.do_stuff()


