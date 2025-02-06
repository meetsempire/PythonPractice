import pandas as pd
# 
# fruits = {"Fruit1": 'apple', "Fruit2": 'banana', "Fruit3": 'mango'}
# my_series = pd.Series(fruits,index=["Fruit2","Fruit3"])
# print(my_series)

# series = pd.Series([100, 200, 300], index=['X', 'Y', 'Z'])
# dictionary = series.to_dict()
# print(dictionary)

# data = {
#     'Car_Name': ["X3", "XUV700", "Fortuner"],
#     'Car_made': ["BMW","Mahindra","Toyota"],
#     'Colour': ['Silver', 'Blue', 'Black']
# }
# 
# df = pd.DataFrame(data)
# print(df)

# data1 = pd.Series(['Apple', 'Banana', 'Cherry'])
# 
# # Printing the original series
# print("Original Series:")
# print(data1)
# 
# # Converting to lowercase
# lower_series = data1.str.lower()
# print("\nLowercase Series:")
# print(lower_series)
# 
# # Converting to uppercase
# upper_series = data1.str.upper()
# print("\nUppercase Series:")
# print(upper_series)
# 
# # Count a length
# length = data1.str.len()
# print("The length is:")
# print(length)

data = {
    'Name': ["Alice", "Babita", "Meet"],  
    'Age': [23, 24, 21],
    'City': ['New York', 'Paris', 'Canada']  
}

# Creating a DataFrame
df = pd.DataFrame(data)
print(df)

# Selecting a column
print("Name:\n", df['Name'])
print("Age:\n", df["Age"])

# Adding a new column 'Gender'
df['Gender'] = ["Male", "Female", "Male"]  

print(df)  # Printing updated DataFrame

# Dropping the 'City' column
df.drop('City', axis=1, inplace=True)

# Printing final DataFrame
print(df)