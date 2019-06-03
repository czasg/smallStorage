__goal__ = "test for MongoDB Multi work flows"

"""
0-9: 48->57
a-f: 97->102

thread: 3
0-9:
0
1
2
0
1
2
0
1
2
0
a-f:
1
2
0
1
2
0

thread: 4
0
1
2
3
0
1
2
3
0
1
a-f:
1
2
3
0
1
2

thread: 5
3
4
0
1
2
3
4
0
1
2
a-f:
2
3
4
0
1
2

"""

def filter(thread, index):
    def wrapper(document):
        return not ord(str(document["_id"])[-1]) % thread == index
    return wrapper


documents = [{"_id":"asdsada"}, {"_id":"asdsadb"}, {"_id":"asdsadc"}, {"_id":"asdsadd"}, {"_id":"asdsade"}]

f = [filter(5, 0),filter(5, 1),filter(5, 2),filter(5, 3),filter(5, 4)]
# for document in documents:
#     for i in f:
#         print(i(document))
#     print("********")

# for i in ["a","b","c","d","e","f"]:
#     print(ord(str(i))%5)
# for i in range(10):
#     print(ord(str(i))%5)
