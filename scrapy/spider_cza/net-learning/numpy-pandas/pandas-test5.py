import numpy as np
import pandas as pd

if __name__ == "__main__":
    left = pd.DataFrame({"key":["k0","k1","k2","k3"],
                         "A":["A0","A1","A2","A3"],
                         "B":["B0","B1","B2","B3"]})
    right = pd.DataFrame({"key": ["k0", "k1", "k2", "k3"],
                         "C": ["C0", "C1", "C2", "C3"],
                         "D": ["D0", "D1", "D2", "D3"]})
    # res = pd.merge(left, right, on='key')  # on是指定基于哪一个columns进行合并
    # print(res)

    left1 = pd.DataFrame({"key1": ["k0", "k1", "k2", "k3"],
                          "key2": ["k0", "k1", "k2", "k3"],
                         "A": ["A0", "A1", "A2", "A3"],
                         "B": ["B0", "B1", "B2", "B3"]})
    right1 = pd.DataFrame({"key1": ["k0", "k1", "k2", "k3"],
                           "key2": ["k0", "k1", "k2", "k3"],
                          "C": ["C0", "C1", "C2", "C3"],
                          "D": ["D0", "D1", "D2", "D3"]})
    res = pd.merge(left1, right1, on=['key1', 'key2'])
    print(res)