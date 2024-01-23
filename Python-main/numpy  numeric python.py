import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))


import numpy
arr = numpy.array([1, 2, 3, 4, 5])

print(arr)

#reshape

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)

#along row
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)


#along column
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)


#split difeerent
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3) #3 == box

print(newarr)


#WHERE LOCATE
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

#for find odd no location
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)



print(x)

#sorting
import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

#random 5 number
from numpy import random

x=random.randint(100, size=(5))

print(x)

#float
from numpy import random

x = random.rand(5)

print(x)
