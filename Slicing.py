import numpy as np

# a=np.arange(0,21)
# print(a)
# b=slice(1,20,4)
# print(a[b])

# a=np.arange(0,16)
# print(a)
# print(a[3:])
# print(a[:10])

# a=np.arange(0,12).reshape(3,4)
# print(a[0:2 , 0:3])

# a=np.arange(0,12).reshape(3,4)
# print("Original Array")
# print(a)
# print("Modified araay")
# for x in np.nditer(a):
#     print(x)

# a=np.sqrt([1, 4, 49, 100])
# print(a)

# a=np.array([[1,2,3,4],[5,6,7,8],[40,50,60,70]])
# print(a)
# b=np.reshape(a,(4,3))
# print(b)

# a=np.arange(1,10).reshape(3,3)
# print("Before Ravel:-")
# print(a)
# print("After Ravel:-")
# b=a.ravel()
# print(b)

# a=np.arange(1,13).reshape(4,3)
# print(a)
# b=np.transpose(a)
# print(b)

# a = np.array([[1,2,3],[6,7,8]])
# b = np.array([[4,5]])
# c = np.concatenate((a,b),axis=None)
# print(c)
# print('\n')
# 
# d = np.array([[1,2],[3,4]])
# e = np.array([[5,6]])
# f = np.concatenate((d,e.T),axis=1)
# print(f)
# print('\n')
# 
# g = np.array([[1,2],[3,4]])
# h = np.array([[5,6]])
# i = np.concatenate((g,h),axis=0)
# print(i)
# 
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# c=np.stack((a,b))
# j=np.hstack((a,b))
# print(j)
# print(c)

# d=np.array([1,2,3])
# e=np.array([4,5,6])
# f=np.column_stack((a,b))
# print(f)
# h=np.vstack((d,e))
# print(h)

# a=np.arange(16).reshape(4,4)
# print(a)
# b=np.split(a,4)
# print(b)

# a=np.arange(16).reshape(4,4)
# print('Horizontal Split')
# [b,c]=np.hsplit(a,2)
# print('B=',b)
# print('C=',c)
# 
# print('Vertical Split')
# [d,e]=np.vsplit(a,2)
# print('D=',d)
# print('E=',e)

# a = np.mod(np.arange(11),3)
# print(a)

# b = np.log([1, np.e, 10])
# print(b)

# x =np.bitwise_or (9, 10)
# print(x)

# x= ([np.log(-1), 1., np.log(0)])
# y= np.isnan(x)
# print(y)

# a =np.arange(12)
# print(a)
# print(a.min())
# print(a.max())
# print(a.mean())
# print(a.sum())
# print(a.std())

# x= np.all([[True, False], [True, True]], axis=1)
# print(x,'\n')
# 
# y= np.all([[True, False], [True, True]], axis=0)
# print(y,'\n')
# 
# z= np.all([[True, False], [True, True]])
# print(z,'\n')
# 
# a= np.all([1,3,5,7,8,9,0])
# print(a)

arr = np.array([1, 2+3j, 4, 5+0j, 6j, 7])

complex_mask = np.iscomplex(arr)

print("Array:", arr)
print("Complex Number Mask:", complex_mask)
print("Complex Numbers in Array:", arr[complex_mask])