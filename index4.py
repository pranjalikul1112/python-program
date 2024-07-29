#function
#def calc_sum(a, b):
 #   sum = a + b
  #  print(sum)
   # return sum
#calc_sum(5,5)

#calc_sum(2,2)

#calc_sum(4,4)
#function definition
#def calc_sum(a, b):#parameters
 #   return a + b
#sum = calc_sum(123,345)#function call; argumentS
#print(sum)

#def print_hello():
 #   print("hello")
#print_hello()

#average of 3 numbers
#def calc_avg(a, b, c):
 #   sum = a + b + c
  #  avg = sum / 3
   # print(avg)
    #return avg
#calc_avg(98,97,96)
#def cal_prod(a=1, b=1):
 #   print(a * b)
  #  return a * b
#cal_prod()
#practice question
#write a  function the length of a list .(list is the parameter)
#cities = ["delhi","gurgaon","noida","pune","mumbai","chennai"]
#heroes = ["thor","ironman","captain america","shaktiman"]

#def print_len(list):
#    print(len(list))

#print_len(cities)
#print_len(heroes)
#write a function the elements of a list in a single line.(list is the parameter)
#cities = ["delhi","gurgaon","noida","pune","mumbai","chennai"]
#heroes = ["thor","ironman","captain america","shaktiman"]

#def print_len(list):
 #   print(len(list))

#def print_list(list):
 #   for item in list:
  #      print(item, end="")
      
#print_list(heroes)
#print()
#write a function find the factorial of n (n is the parameter)
#def cal_fact(n):
    #fact = 1
   # for i in range(1, n+1):
  #      fact *= i
 #   print(fact)

#cal_fact(5)
#write a function convert USD to INR
#def converter(usd_val):
  #  inr_val = usd_val * 83
 #   print(usd_val, "USD=", inr_val, "INR")
#converter(73)
#RECURSION
#def show(n):
 #   if(n == 0):
  #      return
   # print(n)
    #show(n-1)

#show(5)
#def fact(n):
   #if(n == 1 or n == 0):
  #   return 1
 #  return fact(n-1) * n
#print(fact(4))
#pratice question
#write a recursive function to calculate the sum of first n natural numbers
def cal_sum(n):
    if(n == 0):
       return 0
    return cal_sum(n-1) + n
sum = cal_sum(10)
print(sum)
#write a recursive function to print all element in a list [hint:use list and index as parameter]
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

family = ["mummy","pappa","chitu","gitu","bhaiya"]

print_list(family)