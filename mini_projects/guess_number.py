#  Guess the number 
import random


# generate a random number 
random_number = random.randint(1,100)

# ---- using recursion ---------
def guess_Number():
    # input the user 
    user_input = int(input("Please enter a number : "))

    # check if it is larger and smaller and tell him if you win
    if(user_input > random_number):
        print("Number you have entered is larger than expected number")
        guess_Number()
    elif(user_input< random_number):
        print("Number you have entered is smaller than expected number")
        guess_Number()
    else:
        print("🎉congratulation you have guess the number right")

# guess_Number()        

# ----------- using loops ----------
        

while True:
    user_input = int(input("Please enter a number : "))
    if(user_input > random_number):
        print("Number you have entered is larger than expected number")
       
    elif(user_input< random_number):
        print("Number you have entered is smaller than expected number")
        
    else:
        print("🎉congratulation you have guess the number right")
        break
