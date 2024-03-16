## Loops

# while loop
x = 0
while x<=4:         # execute code inside it until condition is true
    if(x==2):
        break       # if i==2, terminate the loop
    if(x==4):
        continue    # if i==4, terminate current iteration and get to next iteration
    print(x)  
    x+=1

# for loop 
    
list = [1,2,3,4]    # we could use tuple , strings , dictionary and set 

for el in list:
    print(el)

# for loop with else 
   
list = [1,2,3,4]

for el in list:
    print(el) 
else: 
    print("END")     # work when loops end, NOT EXECUTE IF WE BREAK LOOP

# range -> it return the sequence , range(start?,end,step?)

seq = range(5)             # output ->  range(0,5), seq[0] = 0, seq[2] = 2
seq = range(1,5,2)         # output ->  range(1, 5, 2), seq[0] = 1, seq[1]=3

for i in seq: 
   print(i)                # output -> 1,3

# pass statement -> can also use in if else also

for i in range(5):
    pass                   # we created it but we want to write code in future here so we can't leave it here hence pass 

                  