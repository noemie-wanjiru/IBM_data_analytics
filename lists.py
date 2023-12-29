#create a list
list=[1, "hello", [1,2,3], True] 
#retrieve a value stored at index 1
print(list[1])
#retrieve a value stored at index, 1,2,3
print(list[1:4])
#retrieve values from multiple indexes 
print(list[1:3],list[2:4])
#concatenate lists
a=[1,"a"]
b=[2,1,"d"]
c=a+b
print (c)
#create empty list 
shopping_list=[]
shopping_list=["Watch","Laptop","Shoes","Pen","Clothes"]
#add new item to the list (.append(), or .extend() for more than 1 item)
shopping_list.append("Football")
print(shopping_list[0])
#print last item on the list
print(len(shopping_list))
print(shopping_list[-1])
#print entire shopping list
print(shopping_list[0:7])
#print laptop and shoes (slicing can be used to print the two)
print(shopping_list[1:3])
#change an item from the shopping list
shopping_list[3]="Notebook"
#delete item from shopping list
del (shopping_list[4])
#print entire shopping list
print(len(shopping_list))
print(shopping_list[0:6])
# copy and clone list 
#copy 
a=[4,5,6]
b=a
a[1]=10
print (a)
print (b)
#clone
c=a[:]
a[1]=11
print(a)
print(c)
