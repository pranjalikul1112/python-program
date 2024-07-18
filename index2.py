#info = {
 #   "name" : "apnacollege",
  #  "subjects" : ["python","c","java"],
   # "topics" : ("dict","set"),
    #"age" : 23,
    #"is_adult" : True,
    #12.99 : 94.4
    #}
#print(info)

  #nested dictionary
#student = {
 #   "name" : "pranjali kul",
  #  "subject" : {
   #     "phy" : 97,
    #    "chem" : 98,
     #   "math" : 98
    
    #}
#}
#print(student["subject"]["chem"])
 #dictionary methods
#keys()
#student = {
 #"name" : "pranjali kul",
  #  "subject" : {
   #     "phy" : 97,
    #    "chem" : 98,
     #   "math" : 98
    
    #}
#}
#print(len(list(student.keys())))
#values
#student = {
 #"name" : "pranjali kul",
  #  "subject" : {
   #     "phy" : 97,
    #    "chem" : 98,
     #   "math" : 98
    
    #}
#}
#print(list(student.values()))
#items
#student = {
 #"name" : "pranjali kul",
     # "subject" : {
    #    "phy" : 97,
   #     "chem" : 98,
  #      "math" : 98
    
 #   }
#}
#pairs = list(student.items())   
#print(pairs[0]) 
#.get
#student = {
 #"name" : "pranjali kul",
  #    "subject" : {
   #     "phy" : 97,
    #    "chem" : 98,
     #   "math" : 98
    
    #}
#}
#print(student["name"])
#print(student.get("name"))  
#update
#student = {
 #"name" : "pranjali kul",
  #    "subject" : {
   #     "phy" : 97,
    #    "chem" : 98,
     #   "math" : 98
    
    #}
#}
#new_dict = {"city" : "pune","age":16}
#student.update(new_dict)
 
#print(student)
#set
#collection = {1,2,2,2,"hello","world","world"}
#print(collection)
#print(type(collection  ))
#sets methods
#collection = set()
#collection.add(1)
#collection.add(2)
#collection.add(2)
#collection.clear()
#print(len(collection))
#collection = {"hello","apnacollege","world","coding","python"}
#print(collection.pop())
#print(collection.pop())
#set1 = {1,2,3}
#set2 = {2,3,4}
#print(set1.intersection(set2))
#print(set1.union(set2))
#print(set1)
#print(set2)
#practice question
#store following word meanings in a python dictionary :
#table :"a piece of furniture","list of facts and figures"
#cat:"a small animal"
#dictionary = {
  #  "cat" : "a small animal",
 #   "table" : ["a piease of furniture","list of facts and figures"]

#}
#print(dictionary)
#you are given a lsit of subjects for students.Assume one classroom is required for 1 subject how many classrooms are needed by all students.
#"python","java","c++","python","javascript",
#"java","python","java","c++","c"
#subjects = {
 #   "python","java","c++","python","javascript","java","python","java","c++","c"
#}
#print(len(subjects))
#WAP to enter marks of 3 subjects fom the user and store them in a dictionary start with an empty dictionary and add one by one use subject name as key and marks as value
#marks = {}
#x = int(input("enter phy :"))
#marks.update({"phy" : x})

#x = int(input("enter phy :"))
#marks.update({"chem" : x})

#x = int(input("enter phy :"))
#marks.update({"math" : x})
#print(marks)
 
# figure out a way to store 9 ad 9.0 as separate values in the set (you can take help of built-in data types)
values = {
    ("float",9.0),
    ("int", 9)
}
print(values)