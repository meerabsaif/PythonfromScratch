 # DATA STRUCTURES IN PYTHON
 # Day 3
 # 28 AUG, 23

"""
1. List (similar to array but not same)
2. Tuple
3. Dictionary 
4. Set

"""
#________________________________________________________________________LIST 
#Continuous data is stored, continuous memory allocation.
l1= [1,5,4,7,3,9,8]
l2= [2,54,6.7,"true","hey","how"]
#more than one data type can be stored in a list 

print(l1)                                 #to print list
print(l2)

print(type(l1))                           #to check data type
print(type(l2))

#list is MUTABLE, means it can be changed.

print(l1[0])                                           #(index starts from zero)
print("value of index 5 is", l1[5])
print("value from index 3 to 6 is", l1 [3:6])          #ending index wont be printed

print(l2[3])
print(l2[2:6])                                         #jis index tak print krwana hay ussey next tk likhna hay
print(l2[0:5:2])

#methods of list 
print(l1)
del l1[-1:]                                          #delete last element
print("after deleting the last element", l1)        

l1.sort()                                            #sorts our list
print("after sorting list",l1) 

#updating a list 
l1[1]=7
l2[4]="bye"
print('updated lists',l1,'\t',l2 )                   #use \t to display in tabular form

#to add value at last of list we use "append" function
l1.append([1])                                  
print ("updated list is:",l1)

#remove a value 
l2.remove("true")                                       #on base of value
print ("after removing true from list, list is :",l2)

l1.pop(4)                                               #on base of index
print("after poping the list is", l1)

#to add value at specific index
l2.insert (2,"avalanche")                        #2 is index where we want to add value. avalanche is the value we want to add at the mentioned index.(which is 2) 
print ("after inserting value the list is:",l2)


#______________________________________________________________________TUPLE (similar to list but not same)
tup1=(1,8,3,7,4,4,5,7,8)
print(tup1)                    #to print 
print(type(tup1))              #to check data type

#tuple is immutable, which means it cannot be changed. (unlike list)

#to count repitition of a value 
tup1.count(4)
print("4 is repeated no. of times:", tup1.count(4)) 

#____________________________________________________________________DICTIONARY 
#writing a word or some variable and assigning it a value.
dict1= { "name": "meerab",
  "field": "xyz",
  "age": 19 }


print(dict1)
print(type(dict1))

#operations in dictionary 

print(dict1.items())
print(dict1.keys())
print(dict1.values())
print(dict1.get("name"))

dict1.pop("age")                                 #to remove
print("after removing", dict1)
dict1.clear()                                    #to empty dictionary
print("after clearing dictionary", dict1)

#_________________________________________________________________SET
#a value is not repeated in a set
#memory allocation is random in a set

s1= {1,2,3,34,54}
print(s1)
print(type(s1))

#operations 

s1.add(5)                                       #to add
print("After adding", s1 )

s1.remove(3)
print("after removing", s1)                     #to remove 