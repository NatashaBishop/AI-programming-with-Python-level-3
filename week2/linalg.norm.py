#liner algebra approach to compute of the magnitude of a 1D vector
import numpy as np

r1= np.array([2,3])
mag=np.linalg.norm(r1)
direction=np.linalg.norm(r1, ord=1)
print(f'The Mag of [2,3] is {direction}')




