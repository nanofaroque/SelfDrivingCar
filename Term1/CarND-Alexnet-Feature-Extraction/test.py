from scipy.misc import imread
import  numpy as np
im1 = (imread("poodle.png")[:, :, :3]).astype(np.float32)
print (im1)
print(im1.size)