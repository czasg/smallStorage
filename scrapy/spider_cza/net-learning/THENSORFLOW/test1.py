import tensorflow as tf
"""
1、创建节点
2、创建会话
3、运行，也就是在会话中添加节点
"""

if __name__ == "__main__":
    # 创建一个常量运算符，将作为一个节点加入到默认计算图中
    hello = tf.constant("Hello, cza's world~")
    # 创建一个TF对话
    session = tf.Session()
    # 运行并获取结果
    print(session.run(hello))