import numpy as np

arr=np.array([[[1, 4, 5, 7, 8], [3, 6, 7, 9, 0]], [[5, 6, 9, 1, 2], [5, 7, 9, 0, 2]]])
print(arr.ndim)
print(arr[1, 1, 3])
print(arr[0, 1, -4]) #Negative indexing will count from backwards
print(arr[0,0,-1]) #[1, 4, 5, 7, 8] from this array -1 index is '8'