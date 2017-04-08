# NOTE: You don't need to edit this code.
import time
import tensorflow as tf
import numpy as np
from scipy.misc import imread
from caffe_classes import class_names
from alexnet import AlexNet


# placeholders
x = tf.placeholder(tf.float32, (None, 227, 227, 3))

# By keeping `feature_extract` set to `False`
# we indicate to keep the 1000 class final layer
# originally used to train on ImageNet.
probs = AlexNet(x, feature_extract=False)   # Finding the probabilities by using alexnet
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# Read Images
im1 = (imread("poodle.png")[:, :, :3]).astype(np.float32)
im1 = im1 - np.mean(im1)

im2 = (imread("weasel.png")[:, :, :3]).astype(np.float32)
im2 = im2 - np.mean(im2)

# Run Inference
t = time.time()
output = sess.run(probs, feed_dict={x: [im1, im2]}) # pass two images as input to the alex net

# print the output shape--> (2, 1000)
# two image creates two rows and 1000 class
print ('output shape: '+ str(output.shape))

# Print Output
for input_im_ind in range(output.shape[0]):
    inds = np.argsort(output)[input_im_ind, :]
    print("Image", input_im_ind)
    for i in range(5):
        print("%s: %.3f" % (class_names[inds[-1 - i]], output[input_im_ind, inds[-1 - i]]))  # print first five most probable results
    print()

print("Time: %.3f seconds" % (time.time() - t))
