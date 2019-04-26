class Test():
    @classmethod
    def solution1(cls, nums, target):
        dict = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in dict:
                return [dict[diff], index]
            dict[num] = index
        return None

    @classmethod
    def solution2(cls, nums, target):  # 有很大的问题=0=
        for i in range(len(nums)):
            for j in reversed(range(len(nums))):
                if i < j and nums[i] + nums[j] == target:
                    return [i, j]
        return None


testSet = {"nums": [3, 7, 12, 15], "target": 19, "res": [1, 2]}
