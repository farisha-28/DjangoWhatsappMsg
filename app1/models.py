from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time

class Users(models.Model):
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
        user_data = Users.objects.all()
        message = MessageHandler.objects.first().message
        return user_data, message

    def __str__(self):

        user_data, user_message = self.get_user_data()
        print("User Data:----", user_data)
        for user in user_data:
            print(f"Name: {user.name}, Phone Number: {user.phone_number}, Email: {user.email_address}, Track ID: {user.track_id}")
        
        users_names = [user.name for user in user_data]
        
        users_phone_numbers = [user.phone_number for user in user_data]
        print("\nUser Phone Numbers:")
        print(users_phone_numbers)

        national_numbers = [phone_number.national_number for phone_number in users_phone_numbers]
        print(national_numbers)

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        link = 'https://web.whatsapp.com'
        driver.get(link)
        
        for n in national_numbers:

            print("**********  ", n , user_message)
            link2 = f'https://web.whatsapp.com/send/?phone=880{n}&text=Hello there!{user_message}'
            driver.get(link2)
            time.sleep(100)
            action = ActionChains(driver)
            action.send_keys(Keys.ENTER)
            action.perform()
            time.sleep(10)

        time.sleep(2000)

class EmailSender(models.Model):
        
        def get_user_data2(self):
            user_data2 = Users.objects.all()
            user_email = MessageHandler.objects.first().email
            return user_data2, user_email

        def __str__(self):
            user_data2, user_email = self.get_user_data2()

            for user in user_data2:
                subject = "This is a test mail from Django"
                message_body = f"Hello {user.name}!\n\n{user_email}"
                from_email = "hfarisha06@gmail.com" 

               
                send_mail(subject, message_body, from_email, [user.email_address])
  

