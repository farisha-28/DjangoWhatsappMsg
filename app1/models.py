from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time

class Message(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=True)
    email_address = models.EmailField(blank=True) 
    track_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class MessageHandler(models.Model):

    DEFAULT_MESSAGE = "Default message"  
    message = models.TextField(default= DEFAULT_MESSAGE)
    DEFAULT_EMAIL = "Default email"  
    email = models.TextField(default= DEFAULT_EMAIL)

    def __str__(self):

        return self.message
        
       
class WhatsappSender(models.Model):

    def get_user_data(self):
        user_names = list(Message.objects.values_list('name', flat=True))
        user_numbers = list(Message.objects.values_list('phone_number', flat=True))
        user_mess = list(MessageHandler.objects.values_list('message', flat=True))
       
        return user_names, user_numbers, user_mess

    def __str__(self):
        user_names, user_numbers, user_mess = self.get_user_data()

        national_numbers = [phone_number.national_number for phone_number in user_numbers]
        print(national_numbers)

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        link = 'https://web.whatsapp.com'
        driver.get(link)
        time.sleep(2000)
        
        for n in national_numbers:

            link2 = f'https://web.whatsapp.com/send/?phone=880{n}&text={user_mess[0]}'
            driver.get(link2)
            time.sleep(100)
            action = ActionChains(driver)
            action.send_keys(Keys.ENTER)
            action.perform()
            time.sleep(10)
    
