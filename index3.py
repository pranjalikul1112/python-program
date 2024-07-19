#while Loop 
#count = 1
#while count <= 5 :
 #   print("hello")
  #  count +=1
#print(count)
#print numbers from 1 to 5
#i = 1
#while i <=5:
 #   print(i)
  #  i +=1
   # print("loop ended") 
#practice question
#print numbers from 1 to 100
#i = 1
#while i <= 100:
 #   print(i)
 #   i += 1
#print numbers from 100 to 1
#i = 100
#while i >= 1:
 #   print(i)
  #  i -= 1
#print the multiplication table of a number n.
#n = int(input("enter number : "))
#i = 1
#while i <= 10:
 #   print(n*i)
  #  i += 1
    #print the element of the following list using a loop:
   # [1,4,9,16,25,36,49,64,81,100]
#nums = [1,4,9,16,25,36,49,64,81,100]
#idx = 0
#while idx < len(nums):
    #print(nums[idx])
    #idx += 1
#search for a number x in this tuple using loop:
#[1,4,9,16,25,36,49,64,81,100]
 #nums = [1,4,9,16,25,36,49,64,81,100]
#x = 36
#i = 0
#while i < len(nums):
 #   if(nums[i] == x):
  #    print("FOUND at idx",i)
#else:
 #   print("finding..")
  #  i += 1
#break statement
#i = 1
#while i <= 5:
 #   print(i)
  #  if(i == 3):
   #     break
    #i += 1
#print("end of looped")
#continue 
#i = 0
#while i <= 5:
 #   if(i == 3):
  #      i += 1
   #     continue
    #print(i)
    #i += 1
#for loop
#nums = [1,2,3,4,5]
#for val in nums:
 #   print(val)
#str = "pranjali"
#for char in str:
 #   print(char)
#else:
 #   print("end")
#practice 
# using for
#print the element of the following list using a loop
#[1,4,9,16,25,36,49,64,81,100]
#nums = [1,4,9,16,25,36,49,64,81,100]

#for el in nums:
   # print(el)
#search for a number x in this tuple using loop:
#[1,4,9,16,25,36,49,64,81,100]
#nums = (1,4,9,16,25,36,49,64,81,100,49)
#x = 49
#idx = 0
#for el in nums:
 #   if(el == x):
 #       print("number found at idx", idx )
 #       idx += 1
#range
#seq = range(5)
#for i in seq:
 #   print(i) 
#practice question
#using for and range()
#print numbers from 1 to 100.
#for i in range(1,101):
 #  print(i)
     
#print numbers from 100 to 1
#for i in range(100,0,-1):
 #   print(i)
#print the multiplication table of a number n
#n = int(input("enter number : "))
#for i in range(1, 11):
 #   print(n * i)
#pass statement
#for i in range(5):
 #   pass
#print("some useful work")
#practice question
#write to find the sum of first n numbers (using while)
#n = 5
#sum = 0
#while i <= n:
    #sum += i
    #i += 1
# print("total sum =", sum)
#write to find the factorial of first n numbers(using for)
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial =",fact)