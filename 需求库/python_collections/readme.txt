from collections import deque
-> it is list of both-way, which mean you will add or delete data left or right
dq = deque([1,2,3])
dp.append(4)  -> add right
dp.appendleft(0)  -> add in the left
dp.pop()  -> pop data most the right side
dp.popleft()  -> on the contrary, delete data most the left side

