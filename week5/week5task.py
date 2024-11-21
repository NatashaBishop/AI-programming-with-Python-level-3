#using np library, implement matrix multyplication of matrix O and p
#use the dot, matmul, @ methods

#install numpy from terminal: pip install numpy
import numpy as np 
O = [[2,5,3],[3,5,8]]
P = [[6,5,1],[3,5,7]]
Ovectorized=np.array(O)
Pvectorized=np.array(P) # can be transposed another way: PvectorizedAndTransposed=np.array(P).T
Ptransposed=Pvectorized.T

result4matmul = np.matmul(Ovectorized,Ptransposed)
result4matmul = np.dot(Ovectorized,Ptransposed)
result4at = Ovectorized@Ptransposed
print(result4matmul)
print(result4matmul)
print(result4at)
