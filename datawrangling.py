import pandas as pd
#obtain dataset from the web
from urllib.request import urlretrieve
url=("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv")
filename="used_cars.csv"
urlretrieve(url, filename)

#create a python list headers of the header names 
headers =["Symboling","Normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
#use pandas method read_csv() to load dat from the web address and set the parameter "names" equal to the python list "headers"

df=pd.read_csv(filename,names=headers)

#return first 10 rows of the dataset
df.head(10)
print(df.head(10))

#replace missing values (?) with NaN (Not a Number)
import numpy as np
df.replace("?", np.nan, inplace=True)
print(df.head(10))

#evaluating for missing values
#1. .isnull()
#2. .notnull()
# You can also count the missing values in each column (using a for loop)
missing_data=df.isnull()

print(missing_data.head(5))
#count number of missing values in each column
for column in missing_data.columns.values.tolist():

    print(missing_data[column].value_counts())
    print("")
# How to deal with missing values 1. drop the whole row or column 
#2. replace data (mean, frequency or other function)
#Replace with average (normalized, bore, stroke, horsepower, peak-rpm,)
    
avg_norm_loss=df["Normalized-losses"].astype("float").mean(axis=0)
print("average of normalised-losses:", avg_norm_loss)
df["Normalized-losses"].replace(np.nan,avg_norm_loss, inplace=True)

avg_bore=df["bore"].astype(float).mean(axis=0)
df["bore"].replace(np.nan,avg_bore,inplace=True)

avg_stroke=df["stroke"].astype(float).mean(axis=0)
df["stroke"].replace(np.nan,avg_stroke,inplace=True)

avg_horsepower=df["horsepower"].astype("float").mean(axis=0)
df["horsepower"].replace(np.nan,avg_horsepower, inplace=True)

avg_peakrpm=df["peak-rpm"].astype("float").mean(axis=0)
df["peak-rpm"].replace(np.nan,avg_peakrpm,inplace=True)

    #1. drop row (in this case we drop every row with the price missing, there is no way to estimate the price)
df.dropna(subset=["price"], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
#using frequency to replace missing values value_counts()gives the unique items in a column idmax()give the most frequent
print("most frequent number of doors: ",df["num-of-doors"].value_counts().idxmax())
df["num-of-doors"].replace(np.nan,"four", inplace=True)

missing_data=df.isnull()
for column in missing_data.columns.values.tolist():

    print(missing_data[column].value_counts())
    print("")
#standardising data (Standardization is the process of transforming data into a common format, allowing the researcher to make the meaningful comparison.)In this case converson of 
    #miles per gallon to litre per kilometer l/100km=235/mpg
df["city-mpg"]=235/df["city-mpg"]
df["highway-mpg"]=235/df["highway-mpg"]
df.rename(columns={"city-mpg":"city-L/100km","highway-mpg":"highway-L/100km"},inplace=True)

#normalization of data using simple feature scaling xnew=(xold/xmax) width and height columns 
df["width"]=df["width"]/df["width"].max ()
df["height"]=df["height"]/df["height"].max ()
print(df.head(15))

    