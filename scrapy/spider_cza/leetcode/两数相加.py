class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Test():
    @classmethod
    def solution1(cls, l1, l2):
        # singly-linked list to int
        def _sll2int(sll):
            res = []
            while sll:
                res.append(sll.val)
                sll = sll.next
            return int("".join([str(val) for val in res[::-1]]))

        # int to singly-linked list
        def _int2sll(num):
            # poor = [ListNode(int(val)) for val in str(num)]
            # res = temp = poor.pop()
            # while poor:
            #     temp.next = poor.pop()
            #     temp = temp.next
            # return res
            # 此处返回一个链表，不适用与此处的测试，下面重写
            return [int(val) for val in str(num)][::-1]

        # main
        res = _sll2int(l1) + _sll2int(l2)
        return _int2sll(res)


class ListLine(object):

    def __init__(self, datalist, *args, **kwargs):
        import logging
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.DEBUG)
        if isinstance(datalist, list) or isinstance(datalist, tuple):
            if datalist:
                self.head = ListNode(datalist[0])
                variable = self.head
                for data in datalist[1:]:
                    variable.next = ListNode(data)
                    variable = variable.next
            else:
                self.head = None
                self.log.info("line list is None now")
        else:
            self.head = None
            self.log.error("input must be list or tuple")

    def isEmpty(self):
        if self.head:
            return False
        else:
            return True

    def getLength(self):
        if self.head:
            count = 1
            temp = self.head
            while temp.next:
                count += 1
                temp = temp.next
            return count
        else:
            return 0

    def append(self, val):
        listnode = ListNode(val)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = listnode
            self.log.info("Done, insert success")
        else:
            self.head = listnode
            self.log.info("list is None, and have set val to head")

    def pop(self):
        if self.head:
            if self.getLength() == 1:
                self.head = None
                return
            pre = temp = self.head
            while temp.next:
                pre, temp = temp, temp.next
            pre.next = None
            return temp.val
        else:
            self.log.error("line list is already None, no value to pop")

    def insert(self, index, val):
        listnode = ListNode(val)
        if self.head:
            pre = temp = self.head
            count = 0
            if count == index:
                self.head = listnode
                listnode.next = temp
                return
            while temp.next and count < index:
                pre, temp = temp, temp.next
                count += 1
            if count == index:
                pre.next = listnode
                listnode.next = temp
            else:
                temp.next = listnode
        else:
            self.head = listnode

    def delete(self, index):
        if self.head and index < self.getLength():
            pre = temp = self.head
            count = 0
            if count == index:
                self.head = temp.next
                return
            while temp.next and count < index:
                pre = temp
                temp = temp.next
                count += 1
            pre.next = temp.next
        else:
            self.pop()

    def find_by_index(self, index):
        if self.head and index < self.getLength():
            temp = self.head
            count = 0
            while temp.next and count < index:
                temp = temp.next
                count += 1
            return temp.val
        else:
            self.log.error("out of range, No valid list or index")

    def find_by_value(self, value):
        pass

    def __str__(self):
        list = []
        temp = self.head
        while temp:
            list.append(temp.val)
            temp = temp.next
        return "->".join(map(lambda val: str(val), list))  # [str(v) for v in list]

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.find_by_index(item)
        elif isinstance(item, slice):
            start, stop = item.start, item.stop
            if start is None: start = 0
            if stop is None: stop = self.getLength()
            list = []
            for i in range(start, stop):
                list.append(self.find_by_index(i))
            return "->".join(map(lambda v: str(v), list))


testSet = {"l1": ListLine([2, 4, 3]).head,
           "l2": ListLine([5, 6, 4]).head,
           "res": [7, 0, 8]}

if __name__ == "__main__":
    line = ListLine([1, 2, 3, 4, 5])
    print(line, " long:", line.getLength())
    line.append(6)
    print(line, " long:", line.getLength())
    line.pop()
    print(line, " long:", line.getLength())
    line.insert(4, 666)
    print(line, " long:", line.getLength())
    # line.delete(6)
    # print(line, " long:", line.getLength())
    print(line[:3], line[3:])
    # print(line[4])
    # print(line.isEmpty())
