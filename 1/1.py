## creating a variable , python is implicit

name = "Abhimanyu"   # assigning  a string to a variable
age = 23             # assigning a integer 
price = 12.34        # assigning a float 
isDeveloper = True   # assigning a boolean

age2 = age           # now age2 have 23 value
print("| name : ", name , " | age : ", age , " | price : " , price )


## checking type of my variable

print(type(name))           # type - <class 'str'>
print(type(age))            # type - <class 'int'>
print(type(price))          # type - <class 'float'>
print(type(isDeveloper))    # type - <class 'bool'>
  
## expressions 

a,b = 2,3                  # multiply string and number
txt = "a"                   
print(2*txt*3)             # output ->  aaaaaa

a,b = 2,3.4                # airthemetic expression between float and int, gives us float
print(b/a)                 # output -> 1.7

a,b = 2,3.4                # integer division, gives integer (but displayed as float)
print(b//a)                # output -> 1.0

## Inputs

name  = input("Please enter your name : ")            # string input
age   = int(input("Please enter your age : "))        # age input
price = float(input("Please enter your price : "))    # prive input

print("| name : ", name , " | age : ", age , " | price : " , price )

## conditions, python is identation (means spacing matters)

if(1 > 2):                                            # false - hence don't execute
    print("if is true")
elif(2>3):                                            # false - hence don't execute
    print("elif is true")
else:                                                 # if no condition is true above - execute
    print("nothing is true")                          
                                                      # output - `nothing is true`

## single line conditions

# terenary operator
age = int(input("Please enter your age : "))    
isEligible = True if age > 18 and age < 21 else False              # if age > 18 and age < 21 , then set isEligible to true else false
print(isEligible)    

# clever if operator
age = int(input("Please enter your age : "))    
isEligible = (True , False) [age > 18 and age < 21]                # if condition inside [] is true , then set first value else 2nd

## type 

# type coversion -> python automatically change type for us 
a,b = 1,2
print(type(a/b))                                        # python converted my int to float

# type casting -> we change type by ourself
a = int("3")                                            # now a is an integer
b = float("2")                                          # now b is float 
c = str(32)                                             # now c is string 
d = int("abhi")                                         # Error 
