import random
import string 

# list of possible characters in password
character_list = list(string.ascii_letters + string.digits + string.punctuation)

# function to choose random character from the list of characters 
def getRandomCharacter():
    random_character = random.choice(character_list)
    return random_character

# generate password
def generateRandomPassword(n):
    password = ""
    for el in range(n):
        password += getRandomCharacter()
    return password

password = generateRandomPassword(10)        
print(password)


# using list comprehension [function for i in range(n)] , will going to run the function n times and store return in list 

password = "".join([getRandomCharacter() for i in range(16)])
print(password)
