#append是加在列表最后位
list = [1, 2, 5]
list.append(9)
print(list) #[1, 2, 5, 9]
# 可将树直接放在双端队列里
from collections import deque
queue = deque() #引入了双端队列deque
queue.append(root)