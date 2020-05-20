import string 
import random

#function to generate random letters
def randomcharacter():
    x = random.choice(string.ascii_letters + string.digits + string.punctuation)
    return x

#call randomcharacter() and join letters together for password
lengthofpassword_raw = input("How long would you like your password to be? ")
lengthofpassword = int(lengthofpassword_raw)
i = 1
password = ""
while i <= lengthofpassword:
    y = randomcharacter()
    password = password + y
    i += 1

print(password)