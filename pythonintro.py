#Python basics
#print 
print("hello python!")
#check version of python
import sys
print(sys.version)
print(type("gizmo"))
print (type(12))
print(type("12almo"))
#finding out the largest and smallest number that your system can represent
print(sys.float_info)
#typecasting (converting integers to float)
float(2)
print(type(float(2)))
x=2.1
x=int(x)
print(type(x))
print(x)
#expression that calculates how many hours in 160 minutes
no_of_hours=160/60
print(no_of_hours)
#let x=3+2*2
x=3+2*2
print("x: ", x)
x=input()
y=input()
z=int(x)+int(y)
print (z)
#concatenate
x="nao"
y="mi"
z=x+y
print(z)
#Strings and indexing
#len()returns the number characters in a string 
name="Naomi Wanjiru Maina"
print(len(name)) 
#slicing: obtaining multiple characters from a string
print (name[0:5])
#stride: every nth variable 
print(name[::3])
#concatenate
statement= "My name is " +name
print(statement)

#escape sequences new line \n tab \t include backslash\\ or r before the string
print("My name is\n naomi")
print("My name is \t naomi")
print("My name is \\naomi")

#string manipulation operations 
#.upper(), converts to upper case .find()finds the position of a variable in a string, .split() split the string into two parts 
name=name.upper()
print(name)

print(name.find("WANJIRU"))
name=name.replace("NAOMI", "ESTHER")

print(name)


