#using np library, implement matrix multyplication of matrix O and p
#use the dot, matmul, @ methods
import numpy as np
O = [[2,5,3],[3,5,8]]
P = [[6,5,1],[3,5,7]]
Ovectorized=np.array[O]
Pvectorized=np.array[P]


result4matmul = np.matmul(Ovectorized,Pvectorized)
result4matmul = np.dot(Ovectorized,Pvectorized)
result4at = Ovectorized@Pvectorized
