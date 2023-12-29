soundtrack_dic={"the bodyguard":"1992","saturday night fever":"1997" }
print(soundtrack_dic.keys())
print(soundtrack_dic.values())
album_sales_dic= {"back in black":50,"the bodyguard":50,"thriller":65}
print("total sales for thriller: ",album_sales_dic["thriller"])
#multiple values for one key
product_details_dic= {}
#adding details to the inventory
ProductNo1 = "Mobile Phone"
ProductNo1_quantity = 5
ProductNo1_price = 20000
ProductNo1_releaseYear= 2020
product_details_dic["ProductNo1"]= ProductNo1
product_details_dic["ProductNo1_quantity"]= ProductNo1_quantity
product_details_dic["ProductNo1_price"]= ProductNo1_price
product_details_dic["ProductNo1_releaseYear"]=ProductNo1_releaseYear

#add more details into the invetory
ProductNo2 = "Laptop"
ProductNo2_quantity = 10
ProductNo2_price = 50000
ProductNo2_releaseYear= 2023
product_details_dic["ProductNo2"]=ProductNo2
product_details_dic["ProductNo2_quantity"]=ProductNo2_quantity
product_details_dic["ProductNo2_price"]=ProductNo2_price
product_details_dic["ProductNo2_releaseYear"]=ProductNo2_releaseYear

#display current products in the inventory
print(product_details_dic)

#check if certain variables are in the inventory 
print("ProductNo1_releaseYear" in product_details_dic)
print("ProductNo2_releaseYear" in product_details_dic)

#delete releaseYear from the dictionary
del(product_details_dic["ProductNo1_releaseYear"])
del(product_details_dic["ProductNo2_releaseYear"])

print(product_details_dic)
