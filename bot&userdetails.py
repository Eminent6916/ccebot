#110922
#Godhelpme

#
"""
    install SpeechRecognition
    install PyAudio to use mic.
    install pywhatkit to search

"""
import random
import re
from urllib import response
user_detail = {}
greeting =['Hi', 'Hello', 'Hey', 'Howdy', 'compliment of season']


def user_det():
    user_detail['username'] = input('Username:\n')
    user_detail['suramename'] = input('Surname:\n')
    user_detail['middlename'] = input('Middle Name:\n')
    user_detail['lastname'] = input('Last Name:\n')
    user_detail['gender'] = input('Gender:\n')
    user_detail['language'] = input('Language:\n')
    user_detail['country'] = input('Country:\n')
    
def bio_data():
    for info, details in user_detail.items():
        print(f'{info}: \t{details.title()}')
    print(' \tDone!.\n \n \nIf any of the above information need adjustment kindly reply with: \n\"Adjust my bio data\"')
    

user_det()
def greet_user(username):
    print(f'\n{random.choice(greeting)} {username}!\n')


def verify_text():
    print(f'\n{random.choice(greeting)} {user_detail["lastname"]} You\'ve successfully filled your bio data.\n By default I am CCE_Bot I will like you to provide and setup brief data for, by given me a sweet name you\'ll like to call me.')


greet_user(user_detail['username'])
bio_data()
user_det()
verify_text()

# response= input(' :> ')
# if response.lower() == "Adjust my bio data":

#started this and abandon it many times but i guess this is non-stop pick up. 