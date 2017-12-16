import tensorflow as tf
deep_learning=tf.constant('Deep Learning')
session = tf.Session()
session.run(deep_learning)
a = tf.constant(2)
b = tf.constant(3)
multiply = tf.multiply(a,b)
session.run(multiply)