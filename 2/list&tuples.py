## Lists

# basic 
marks = [1,2,"hello",4,True]
print(type(marks))                       # output -> <class 'list'>
print(marks[0] , " and " , marks[2])     # output -> 1 and hello
print(len(marks))                        # output -> 5
    
# mutable 
marks[1] = "bye"                         # allowed (if you do similar thing in string -> Error)

# slicing -> list[starting_idx : ending_idx], ending_idx not included
print(marks[0:3])                     # output -> [1, 'bye', 'hello']
print(marks[:3])                      # output -> [1, 'bye', 'hello'] , similar to [0:3]
print(marks[2:])                      # output -> ['hello', 4, True] , similar to [2: len(marks)]

# negative index -> start with -1 and -1 means last element
print(marks[-1])                             # output -> True
print(marks[-3])                             # output -> hello
print(marks[-3:-1])                          # output -> ['hello', 4]

# some important methods , below methods does'nt return anything. They change the real  
marks.append("element")                      # add one element in the end
marks.sort()                                 # sort in ascending order, but all element should be of same type
marks.sort(reverse=True)                     # sort in descending order, but all element should be of same type
marks.reverse()                              # reverse list
marks.insert(2,"nothing")                    # adding "nothing" at index 2
marks.remove("hello")                        # remove first occurance of "hello"
marks.pop(1)                                 # remove element at index 1

new_marks = marks.copy()                     # copying marks list 
print(new_marks == marks)                    # output -> True

"".join(["a","b","c"])                       # outpur -> abc

#---------------------------------------------------------------------------------------------------------------------------------------------------

## Tuples

# basic
tup = (1,2,3,4,"hello")
print(type(tup))                           # output -> <class 'tuple'>
print(tup[0] , " and " , tup[2])           # output -> 1  and  3 
print(len(tup))                            # output -> 5 

# single_value_tuple 
new_tup = (1,)                             

# immutable
tup[1] = 2                                 # Error -> assigning not allowed

# some important methods
tup.index("hello")                         # return index of 1st occurance of "hello"
tup.count("hello")                         # count total occurances 

