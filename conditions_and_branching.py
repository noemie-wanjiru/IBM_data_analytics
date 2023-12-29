#comparison operators 
#equal: ==
#not equal: !=
#greater than: >
#less than: <
#greater than or equal to: >=
#less than or equal to: <=

#logical operators (and, or, not)
#Write an if statement to determine if an album had a rating greater than 8. Test it using the rating for the album “Back in Black” that had a rating of 8.5. If the statement is true print "This album is Amazing!"
album_rating=input()
if album_rating> 8:
    print ("This album is amazing!")

#Write an if-else statement that performs the following. If the rating is larger then eight print “this album is amazing”. If the rating is less than or equal to 8 print “this album is ok”.
album_rating=input()
if album_rating> 8:
    print ("This album is amazing!")
else:
    print("This album is okay")

#Write an if statement to determine if an album came out before 1980 or in the years: 1991 or 1993. If the condition is true print out the year the album came out.
album_year_release=input()
if album_year_release<1980:
    print("The album was released before 1980")
elif album_year_release = 1991 or album_year_release=1993:
    print("This album was released in 1991 or 1993")