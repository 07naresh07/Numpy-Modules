import numpy as np
arr = np.array([3, 4, 5, 6, 7])
arr1 = np.array(['tea','yeah'])
print(arr.dtype)
print(arr1.dtype)
arr2 = np.array([4, 1, 2, 9, 7], dtype='f') #Changes datatype to float
print(arr2)
print(arr2.dtype)
arr3 = np.array([4, 1, 2, 9, 7], dtype='i4') #Changes datatype to integer 32bits (maybe)
print(arr3)
print(arr3.dtype)