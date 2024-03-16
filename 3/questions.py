# function to calc length of list
def lengthOfList(list):
     print(len(list))
     return len(list)

lengthOfList([1,2,3,4,5,6,7,8,9])

# caculating a factorial using function and loop

def factorial(n):
    fact = 1 
    for el in range(1,n+1):
         fact*=el
    return fact

num = factorial(5)     
print(num)

# factorial using recursion 

def factorialUsingRecursion(n):
    if(n==0):                     # base case -> very necessary in recursion to stop it
         return 1
    else:
         return n * factorialUsingRecursion(n-1)

number = factorialUsingRecursion(5) 
print(number)

# write a recursive function to print all elements in a list 

def printRec(list,i):
     if(i == len(list)):
          return 1
     else:
       print(list[i],end=" ")
       i+=1
       printRec(list,i)

printRec(["hello","abhi","how","are","you","?"],0)     