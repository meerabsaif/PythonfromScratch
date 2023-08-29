#a basic concept
#for example

a=10
b=20
print(a,b)

#we can also write in form 

c, d = 10, 20 
print(a,b)

#both will give the same output

#lets take another example 
dict1= { "name": "meerab",
  "field": "xyz",
  "age": 19 }
print(dict1.items())

for i , v in dict1.items():
    print("the keys in dictionary are: ",i)
    print("the values in dictionary are:",v)

print(i, ":" ,v)




