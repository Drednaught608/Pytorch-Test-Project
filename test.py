import torch
import numpy as np

ndarray = np.array([0, 1, 2])
t = torch.from_numpy(ndarray)
print(str(t) + '\n')

print(t.shape)
print(t.dtype)
print(t.device)

