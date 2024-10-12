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

