#f = open("demo.txt", "r")
#data = f.read()
#print(data)
#print(type(data))
#f.close() 
#with syntax
#with open("demo.txt", "r") as f:
 #   data = f.read()
  #  print(data)
#with open("demo.txt", "w") as f:
 #   f.write("new data")
#delete
#import os

#os.remove("demo.txt")
#practice question
#create a new file "practice.txt"using python add the folowing data in it:
#hi everyone
#we are learning file I/O
#using java
#I like programming in java
#with open("practice.txt","w") as f:
    #f.write("hi everyone\nwe are learning file I/O\n")
    #f.write("using java.\nI like programming in java.")
#write a file replace all occurrences of java with python in above file
with open("practice.txt", "r") as f:
    data = f.read()
new_data = data.replace("java","python")
print(new_data)
with open("practice.txt", "w") as f:
    f.write(new_data)
#search if the word "learning" exits in the file or not
def check_for_word():

 word = "elearning"
 with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")
check_for_word()