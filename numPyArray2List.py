#Converting one-dimensional NumPy Array to List 

import numpy as np
# list 2 array
arr_1 = np.array([1, 2, 3])
print(f'NumPy Array:\n{arr_1}')
#output:
#NumPy Array:
#[1 2 3]

#array2list with tolist() - this function does mot take any arguments:
list_1 = arr_1.tolist()
print(f'List: {list_1}')
#output:
#List: [1, 2, 3]

#Converting multi-dimensional NumPy Array to List
import numpy as np

# 2d array to list
arr_2 = np.array([[1, 2, 3], [4, 5, 6]])

print(f'NumPy Array:\n{arr_2}')
#output:
#NumPy Array:
#[[1 2 3]
# [4 5 6]]

#Now, let’s use tolist():
import numpy as np
# 2d array to list
arr_2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f'NumPy Array:\n{arr_2}')
list_2 = arr_2.tolist()
print(f'List: {list_2}')
#output:
#List: [[1, 2, 3], [4, 5, 6]]
