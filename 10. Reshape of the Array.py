import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.reshape(2, 3))    #1D to 2D array reshaping
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr1.reshape(3, 3))   #1D to 2D array ith 3X3
arr2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr2.reshape(2, 2, 3))     #1D to 3D array reshape

arr3 = np.array([0,2,3,4,5,6,7,8])
print(arr3.reshape(4, 2).base)  #to check whether given return view or copy. As array returns original array so it is a view

arr4 = np.array(([2, 3, 4, 0], [5, 6, 7, 8]))
print(arr4.ravel()) #Converting 2D array to 1D array
print(arr4.reshape(-1))

arr5 = np.array([[[3, 4, 5], [6, 7, 8]], [[0, 2, 3], [9, 4, 2]]])
print(arr5.flatten())   #3D to 2D array
print(arr5.reshape(-1))