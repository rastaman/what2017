import tensorflow as tf

# model = tf.initialize_all_variables()

a = tf.constant(10, name="a")
b = tf.constant(90, name="b")
y = tf.Variable(a + b * 2, name="y")

model = tf.initialize_all_variables()
with tf.Session() as session:
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter("/tmp/tensorflowlogs", session.graph)
    session.run(model)
    print(session.run(y))
