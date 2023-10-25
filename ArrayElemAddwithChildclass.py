import numpy as np
import array
class myarray:
 arr1 = np.array((1,2,3,4))
 arr2 = np.array([5,6,7,8])
 def array_add(self):
  resultarr=self.arr1+self.arr2
  print('resultarr is')
  return resultarr
    
arrObj=myarray()
arrObj.arr1=np.array([[2,3,4,5],[32,32,23,45]])
arrObj.arr2=np.array([[3,4,5,6],[7,6,5,4]])
resultObj=arrObj.array_add()
print("aray after addition:\n",resultObj)