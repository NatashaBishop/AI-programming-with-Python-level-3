import numpy as np

r1= np.array([2,3])
mag=np.linalg.norm(r1)
direction=np.linalg.norm(r1, ord=1)
print(f'The Mag of [2,3] is {direction}')
