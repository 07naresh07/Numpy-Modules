import numpy as np

arr = np.array(([3, 4, 5, 6], [9, 0, 4, 1]))
print(arr[0, 1:3])
print(arr[1, 2:5])

arr1 = np.array([[[2, 3, 5, 6], [6, 9, 0, 2]], [[9, 1, 2,12], [23, 45, 67, 34]]])
print(arr1[0,1, 0:3])   #3d array slicing
print(arr1[1, 0, -3:-1])    #3d negative slicing