import re

def isValid(phone):

    Pattern = re.compile('[6-9][0-9]{9}')
    return Pattern.match(phone)

phone = input("Enter the phone number:")

if(isValid(phone) and len (phone)==10):
    print(" Entered number is a valid phone number")
else:
    print("Not a valid phone number")
