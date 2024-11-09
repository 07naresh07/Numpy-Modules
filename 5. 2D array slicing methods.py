import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:5, 3])  #Returns 3rd element from each array i.e. first array  and second array
print(arr[0, 0:4])  #Returns elements of 0th array with slising from 0 to 4
print(arr[0:3] [1:3])   #Slicing from 0 to 3 for first array and 1 to 3 for second array and gives 2D array

