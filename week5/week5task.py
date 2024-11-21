import numpy as np
O = [[2,5,3],[3,5,8]]
P = [[6,5,1],[3,5,7]]
Ovectorized=np.array[O]
Pvectorized=np.array[P]
Ptransposed=Pvectorized.T

result4matmul = np.matmul(Ovectorized,Ptransposed)
result4matmul = np.dot(Ovectorized,Ptransposed)
result4at = Ovectorized@Ptransposed
