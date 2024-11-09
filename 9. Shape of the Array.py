import numpy as np

arr = np.array(([4, 5, 7, 0, 2], [9, 1, 2, 6, 8]))
print(arr.shape)    #Shape of the array i.e. 2 arrays with 5 elements in each

arr1 = np.array([[[4, 5, 6], [1, 2, 3], [0, 1, 3]], [[4, 6, 7], [2, 3, 7], [0, 2, 3]], [[6, 7, 8], [9, 3, 9], [5, 8, 9]]])
print(arr1.shape)

arr2 = np.array([5, 8, 9], ndmin=5)
print(arr2, arr2.shape)