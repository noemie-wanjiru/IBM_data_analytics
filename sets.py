#two ways to create a set 1. define as set and add members 2. make a list and typecase the list to a set
#1. 
set1={"pop","rock","soul","hard rock","rock","rnb","dicso"}
#2. convert list to set 
album_list=["pop","rock","soul","hard rock","rock","rnb","dicso", "michael jackson", "Thriller", 46.0,65]
album_set=set(album_list)

#set operations 
#add()
album_set.add(750)
#remove()
album_set.remove("pop")
#vefy element in set
print("pop"in album_set)

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
#intersection of the sets &
intersection=album_set1 & album_set2
print (intersection)
#or .intersection()
print(album_set1.intersection(album_set2))


#only items in set 1 not in set 2
print(album_set1.difference(album_set2))

#union of the sets 
album_set1.union(album_set2)

#superset 
set(album_set1).issuperset(album_set2)

#subset
set(album_set1).issubset(album_set2)


#convert the list to set ["rap","house","electronic music","rap"]
seta=set(["rap","house","electronic music","rap"])

#Consider the list A = [1, 2, 2, 1] and set B = set([1, 2, 2, 1]), does sum(A) == sum(B)?
A=set([1, 2, 2, 1])
B=set([1, 2, 2, 1])
print("sum set A:", sum(A), "\n sum set B:", sum(B))

# create a new set albumset3 that is the union of album_set1 and album_set2
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3=album_set1.union(album_set2)
print(album_set3)
#find out if album_set1 is a subset of album_set3
print(set(album_set1).issubset(album_set3))