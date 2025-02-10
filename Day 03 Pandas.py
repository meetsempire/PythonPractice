import pandas as pd
a = pd.read_csv("Purchase_sales.csv")
print(a)

# selected_0_rows=a.loc[3]
# print(selected_0_rows)
# 
# selected_1_rows=a.iloc[0:3]
# # multiple row
# print(selected_1_rows)

# b= a.drop([3])
# #for single index
# print(b)
# 
# c= a.drop(a.index[0:3])
# # for multiple index
# print(c)
a.loc[3]=['Pajamas',350,4,1400]
print(a)