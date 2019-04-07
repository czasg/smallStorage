import tensorflow as tf
"""
张量的属性
1、零阶张量表示标量（scalar），也就是一个数
2、一阶张量表示向量（vector），也就是一维数组
3、n阶张量可以理解为一个n维数组通过[x,y]，多维类似

获取张量的元素：
一维就是类似下标，二维就可以
"""
if __name__ == "__main__":
    node1 = tf.constant(3.0, tf.float32, name="node1")
    node2 = tf.constant(4.0, tf.float32, name="node2")
    node3 = tf.add(node1, node2)
    # 输出结果不是一个具体数字，而是一个张量的结构
    print(node3)

    session = tf.Session()
    print(session.run(node1))
    print(session.run(node2))
    print(session.run(node3))

    scalar = tf.constant(100)
    vector = tf.constant([1,2,3,4])
    matrix = tf.constant([[1,2,3],[4,5,6]])
    cube_matrix = tf.constant([[1,2,3],[2,3,4],[5,6,7]])
    # 通过get_shape自带函数抓取节点的shape
    print(scalar.get_shape(),session.run(scalar))
    print(vector.get_shape(),session.run(vector)[1])
    print(matrix.get_shape(),session.run(matrix)[1,1])
    print(cube_matrix.get_shape(),session.run(cube_matrix)[1,1])