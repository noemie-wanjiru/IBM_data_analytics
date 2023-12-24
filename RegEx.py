# regEx the re module allows python users to work with regular expressions 
import re
# searh, split, findall, sub
#1. search function (searches for specified patterns in a string) first define pattern, use the search function and check for a match
s1="Michael Jackson is the best"
pattern=r"Jackson"
result=re.search(pattern,s1)
if result:
    print("Match found!")
else:
    print ("Match not found!")

pattern=r"\d\d\d\d\d\d\d\d\d"
text= "My phone number is 123456789"
match=re.search(pattern,text)
if match:
    print("Phone number found:", match.group())
else:
    print("No match")
    #replace (sub) 
g="Mary had a little lamb little lamb, little lamb Mary had a little lamb\n Its fleece was white as snow and everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
pattern="Mary"
replacement="Bob"
g1=re.sub(pattern, replacement,g, flags=re.IGNORECASE)
print(g1)
