import tensorflow as tf
"""
有关操作的介绍：

"""

if __name__ == "__main__":
    tf.reset_default_graph()

    a = tf.Variable(1, name="a")  # 定义变量a
    b = tf.add(a, 1, name="b")  # 定义操作b，即a+1
    c = tf.multiply(b, 4, name="c")  # 定义操作c，即b*4
    d = tf.subtract(c, b, name="d")  # 定义操作d，即c-b

    # session = tf.Session()
    # print(session.run(a))
    # print(session.run(b))
    # print(session.run(c))
    # print(session.run(d))

