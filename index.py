#string
#str1 = "this is a stirng.\n we are creating it in python."
#print(str1)
#string length
#str1 = "pranjali"
#len1 = len(str1)
#print(len1)

#str2 = "kul"
#len2 = len(str2)
#print(len2) 
#final_str = str1+ " "+ str2
#print(final_str)
#print(len(final_str))
#indexing
#str = "pranjalikul"
#ch = str[0]
#print(ch)
#slicing
#str = "pranjali kul"
#print(str[1:4])
#print(str[-1:-4])
#string function

#str = "I am studying python from apna college"
#print (str.endswith("ege"))

#str = "I am studying python from apna college"
#str = str.capitalize()
#print(str)

#str = "I am studying python from apna college"
#print(str.replace("python","java"))

#str = "I am studying python from apna college"
#print(str.find("from"))

#str = "I am studying python from apna college"
#print(str.count("o"))

#practice questions
#write a python program to input user's firsr name and print its length
#name = input("enter your name : ")
#print ("length of your name is",len(name))

#write a python program find the occurrence of $ in a string
#str = "Hi , $Iam the $ symbol $99.99"
#print(str.count("$"))
#Conditional Statements
#age = 24
#if(age >= 18):
 #   print("can vote and apply for license")
#light = "green"

#if(light == "red"):
 #   print("stop")
#elif(light == "green"):
 #   print("go")
#elif(light == "yellow"):
 #   print("look")
  #  print("end of code")
#num = 5
#if(num >2):
 #   print("greater than 2")
#if(num > 3):
 #   print("greater than 3")

#light = "pink"

#if(light == "red"):
    #print("stop")
#elif(light == "pink"):
 #   print("go")
#elif(light == "yellow"):
 #   print("look")
#else:
 #   print("light is broken")
#print("end of code")
#practice program
  #write a python program to check if a number entered by the user is odd or even
#num = int(input("enter number:"))

#rem = num % 2
#if(rem == 0):
 #   print("EVEN")
#else:
   # print("ODD")
#write a python program find the greatest of 3 numbers entered by the users
#a = int(input("enter the first number:"))
#b = int(input("enter the second number:"))
#c = int(input("enter the third number:"))
#if(a >=b and a >= c):
 #   print("first number is largest ")
#elif(b >= c):
 #   print("second number is largest",b )
#else:
 #   print("third is largest",c)
#WAP to check if a number is a multiple of 7 or not
x = int(input("enter  number:"))
if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")