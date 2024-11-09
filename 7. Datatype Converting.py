import numpy as np

arr = np.array(['1', '4', '0', '5'], dtype='i') #Can convert to integers if its all numbers but not if its alphabates
print(arr, arr.dtype)

arr1 = np.array([1.2, 3.4, 6.1, 7.3])
newarr = arr1.astype('i')   #copy the existing array arr1 and converts float to integer using 'astype()'
print(newarr, newarr.dtype)

arr2 = np.array([3, 5, 7, 8])
newarr2 = arr2.astype('S')  #Converts to strings
print(newarr2)

arr3 = np.array([1, 0, 1, 3])
newarr3 = arr3.astype(bool)
print(newarr3, newarr3.dtype)