#create a tuple 
tuple1=("disco",10,1.2)
#print tuple 
print(tuple1)
#print out all values of the tuple individually
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
#print type of variables in the tuple
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

#lenght of tuple 
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", 
                "R&B", "progressive rock", "disco")
print(len(genres_tuple))

#slicing to object objects stored at index 2,3,4
print(genres_tuple[2:5])

#find the index of s in "disco"
print(genres_tuple[7][2])

#sort a tuple 
c_list=sorted(genres_tuple)
print(c_list)