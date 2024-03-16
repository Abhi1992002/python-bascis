# creating a file named "practice.txt",add this data 
# Hi everyone 
# we are learning File I/O
# using java.
# I like java programming

with open("practice.txt", "w") as w:
    w.write("Hi everyone\nwe are learning File I/O\nusing java.\nI like java programming")
   
# replace all occurance of java with python 

with open("practice.txt","r") as r:
    content = r.read()
    new_content = content.replace("java","python")
   

with open("practice.txt","w") as p:
    p.write(new_content)

# check if word learning exist in it or not 

with open("practice.txt","r") as r:
    content = r.read()
    exist = content.find("learning")    
    if(exist != -1):
        print("word 'learning' exist in file. ")
    else:
        print("doesn't exist")

# function to find at which line does "learning" occur first.

def findLine(word = "learning"):
    with open("practice.txt","r") as r:
        data = True 
        line_no = 1
        while(data):
            data = r.readline() #return empty string if no file exist    
            if(word in data):
                print("word ",word," present in file at line number : ",line_no)
                break
            line_no += 1    
        else:
            print("doesn't exist in file")
            return -1

findLine()
    
