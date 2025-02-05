import pandas as pd
# a= pd.read_csv("Purchase_sales.csv")
# print(a)

# a= pd.read_excel("Purchase.xlsx")
# print(a)

# a= pd.read_excel("a1.xlsx")
# print(a)
# 
# import pandas as pd

# Read the Excel file without headers
# df = pd.read_excel("Purchase.xlsx", header=None)
# 
# # Print the dataframe
# print(df)

# Creating a pandas Series with custom index
# fruits = pd.Series([18, 23, 15], index=["Small", "Medium", "Large"])
# 
# # Print the Series
# print(fruits)
# 
# # Extracting values
# a = fruits.values
# print(a)
# 
# # Extracting index
# b = fruits.index
# print(b)
# 
# # Extracting size
# c = fruits.size
# print(c)
# 
# # Extracting shape
# d = fruits.shape
# print(d)

data=[10,20,30,40,50]
a= pd.Series(data)
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

a=[2,4,6]
df=pd.Series(a,index=["x","y","z"])
print(df)
