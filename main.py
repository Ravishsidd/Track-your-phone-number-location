#--------------------Track your phone number location--------------------#
import phonenumbers

#----------geocoder: To know the specific Location to that phone number----------#
from phonenumbers import geocoder

phone_number = phonenumbers.parse("Numbers with country code")
'-----Indian phone number example: +91745*******-----'
'-----Pakistani phone number exanple: +926399******-----'

#----------This will print the country name----------#
print(geocoder.description_for_number(phone_number, 'en'))






