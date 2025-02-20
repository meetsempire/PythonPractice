import pandas as pd

df= pd.read_excel('Student-marks.xlsx')
print(df)

file='Student-marks.xlsx'
sheet1 = pd.read_excel(file, sheet_name=0, index_col=0)
sheet2 = pd.read_excel(file, sheet_name=1, index_col=0)

new_data=pd.concat([sheet1,sheet2])
print(new_data)
print(new_data.shape)

# Ensure column names are consistent with the dataset
column_names = ['English', 'Maths', 'Science']  # Make sure these names match exactly with your dataset

# Sort data in ascending order based on 'English', 'Maths', and 'Science'
sorted_data = new_data.sort_values(by=column_names, ascending=True)

# Select only the required columns
sorted_data = sorted_data[column_names]

# Display sorted data
print(sorted_data)

# a = pd.read_excel('Purchase.xlsx')
# print(a)
# 
# b = a.head()
# # fetch first 5 rows
# print(b)
# 
# c = a.tail()
# # fetch last 5 rows
# print(c)
# 
# d = a.describe()
# print(d)