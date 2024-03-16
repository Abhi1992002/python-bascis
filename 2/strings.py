## strings 

# creation
str1 = "This is a string."
str2 = 'This is also a string.'
str3 = """This is also a string."""

# concatation - adding 2 strings
print(str1 + " " + str2)           # output -> This is a string. This is also a string.

# length of string 
print(len(str1))                   # output -> 17 

# indexing
print(str1[0])                     # output -> T
print(str1[1])                     # output -> h
str1[4] = 'h'                      # Error -> assignment does'nt allow

# slicing : string[starting_idx : ending_idx] 
print(str2[1:4])                   # output -> his  , ending idx character not included 
print(str2[:4])                    # output -> This , simialr to [0 : 4] 
print(str2[1:])                    # output -> his is also a string. , similar to [0 : len(str)] 

# negative index -> start with -1 , and -1 represent last charater
print(str1[-1])                    # output -> .
print(str1[-3 : -1])               # output -> ng

# some important functions of string 
str1.endswith(".")                 # return true if string ends with "."
str1.capitalize()                  # capitalize 1st char
str1.replace("This","That")        # replace "This" with "That" in string
str1.find("is")                    # return 1st index at which "is" comes in string
str1.count("s")                    # count number of time "s" comes in string