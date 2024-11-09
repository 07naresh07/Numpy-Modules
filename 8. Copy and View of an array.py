import numpy as np

arr = np.array([4, 5, 7, 0, 2])
x = arr.copy()  #Creates the copy of the existing array
arr[3]=100  #Replaces index 3 by 100 i.e. 0 by 100
print(arr)  #Prints the modified arr value
print(x)    #Prints the copy of arr i.e. unmodified one
arr1 = np.array([12, 34, 56, 78, 9])
y=arr1.view()   #Creates view of arr1
arr1[0]=10  #Replaces 0 index number with 10
print(arr1)     #Prints the modified arr1
print(y)    #Prints the view of arr1 and shows modified one as change on array affects how we view the array

arr3 = np.array([78, 9, 12, 0])
z = arr3.view()
z[3]=20
print(arr3) #Original array should be affected if we change the view
print(z)

