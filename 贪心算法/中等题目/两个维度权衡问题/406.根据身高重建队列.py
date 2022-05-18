"""
局部最优：优先按身高高的people的k来插入。插入操作过后的people满足队列属性

全局最优：最后都做完插入操作，整个队列满足题目队列属性

"""
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 先按照h维度的身高顺序从高到低排序。确定第一个维度
        # lambda返回的是一个元组：当-x[0](维度h）相同时，再根据x[1]（维度k）从小到大排序（将身高高的排前面，将同意身高的人数排后面）
        people.sort(key=lambda x: (-x[0], x[1]))  # 此时x就是people中的元素
        que = []

        # 根据每个元素的第二个维度k，贪心算法，进行插入
        # people已经排序过了：同一高度时k值小的排前面。
        for p in people:
            que.insert(p[1], p)  # p[1]是位置，p是元素  (这一步很牛皮)
            print(que)
        return que


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
s = Solution()
s.reconstructQueue(people)
