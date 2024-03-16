#  create a sum of first n numbers (using while)

n = 10 
i = 0
sum = 0
while i <= n:
   sum += i
   i+=1
print(sum)

# find factorial of n number (using for):

n = 5
product = 1

for el in range(1,n+1):
   product *= el

print(product)   