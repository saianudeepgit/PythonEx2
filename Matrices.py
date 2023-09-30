import numpy as np
zeroDarray=np.array([1,2,3,4,5])
zeroDarray1=np.array([6])

addDarray=zeroDarray+zeroDarray1
subDarray=zeroDarray-zeroDarray1
mulDarray=zeroDarray*zeroDarray1
divDarray=zeroDarray/zeroDarray1


print("the addition resulted array is :",addDarray)
print("the subration resulted array is :",subDarray)
print("the multiplication resulted array is :",mulDarray)
print("the division resulted array is :",divDarray)

print("the array is :",zeroDarray)
print("the dimension of the array :" ,zeroDarray.ndim)
print("the size of the array :" ,zeroDarray.size)
print("the shape of the array :" ,zeroDarray.shape)

rangeArray = np.arange(2,10,3)
print(rangeArray)
print(rangeArray.size)