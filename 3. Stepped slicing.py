import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[-3:-1]) #Negative slicing
print(arr[1:8:2]) #Stepped slicing, 2-step: starts with 2 as step is 2 and steps every 2 elements
print(arr[0:8:2])
print(arr[::3]) #Stepped slice as 3 digits