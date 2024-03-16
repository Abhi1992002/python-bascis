# file I/O -> reading and writing data 

# type of files , we can manipulate both file 
# 1.) Text files : .txt , .docs , .log etc 
# 2.) Binary files : .mp4 , .mp4 ,.png , .jpeg etc
 
# open ,read & close file 
# f = open("file_name","mode") , mode - read/write, by_default -> read

f = open("read.txt","r")

data = f.read()             # f.read(5) -> want to read first 5 character, if we read it we can't read it again
read_1_line = f.readline()  
read_2_line = f.readline()  

print(data) 
print(type(data))

f.close()
 
# some imoportant mode 

# "r" -> open for reading 
# "w" -> open for writing, delete what is there and then you write it 
# "x" -> create a new file and open it for writing 
# "a" -> open for writing and append my text after what is written in it
# "b" -> binary mode (if we are trying to open binary file) , like rb , wb
# "t" -> text mode (default)
# "+" -> open a disk for updating , r+ -> want to write as well as read , same with w+

# r+ (not truncate) -> read + overwrite -> pointer - starting (we could write anything in start using it )
# w+ (truncate) -> read + overwrite -> complete file deleted initially
# a+ (not truncate) -> read + append.   -> pointer - end


# if file does'nt exist for writing , python will create it automatically
# writing in a file 

w = open("read.txt","w")
w.write("Now my whole data of file changes")
w.close()

# append in a file 
a = open("read.txt","a")
a.write("i am appending this after complete write.")

# creatind a file 
a = open("sample.txt","w")
a.write("creating a file")
a.close()

# reading + writing , differnet from whole file writing , initially you do not delete complete file 
f= open("read.txt","r+")
f.write("hello")            # first five charater is replaced by hello
print(f.read())             # here my f read after hello because pointer is at hello 
f.close()

# better syntax to write (now we do not need to close)

with open("read.txt","r") as f:
        data = f.read()

print(data)

