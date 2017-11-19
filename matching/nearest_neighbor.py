'''
A nearest neighbor learning algorithm to identify closest matching profiles
using the TensorFlow library.

Author: Detonateur Team
Project: https://github.com/rastaman/what2017/
'''

from __future__ import print_function

from beacoachmate import input_data
import numpy as np
import tensorflow as tf

# Import test data
beacoachmate_datas = input_data.read_data_sets("/tmp/data/", one_hot=True)

Xtr, Ytr = beacoachmate_datas.train.next_batch(1000)  # 1000 for training (nn candidates)
Xte, Yte = beacoachmate_datas.test.next_batch(200)  # 200 for testing

# tf Graph Input
xtr = tf.placeholder("vector", [8])
xte = tf.placeholder("vector", [8])

# Nearest Neighbor calculation using L1 Distance
# Calculate L1 Distance
distance = tf.reduce_sum(tf.abs(tf.add(xtr, tf.negative(xte))), reduction_indices=1)
# Prediction: Get min distance index (Nearest neighbor)
pred = tf.arg_min(distance, 0)

accuracy = 0.

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()

# Start training
with tf.Session() as sess:

    # Run the initializer
    sess.run(init)

    # loop over test data
    for i in range(len(Xte)):
        # Get nearest neighbor
        nn_index = sess.run(pred, feed_dict={xtr: Xtr, xte: Xte[i, :]})
        # Get nearest neighbor class label and compare it to its true label
        print("Test", i, "Prediction:", np.argmax(Ytr[nn_index]), \
            "True Class:", np.argmax(Yte[i]))
        # Calculate accuracy
        if np.argmax(Ytr[nn_index]) == np.argmax(Yte[i]):
            accuracy += 1. / len(Xte)
    print("Done!")
    print("Accuracy:", accuracy)
