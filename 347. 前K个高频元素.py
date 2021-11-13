"""
# 1.要统计元素出现频率：首先统计元素出现的频率，这一类的问题可以使用map来进行统计
# 2.对频率排序：可以使用一种 容器适配器就是优先级队列，然后是对频率进行排序
# 3.找出前K个高频元素
"""
# 时间复杂度：O(nlogk)
# 空间复杂度：O(n)
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 要统计元素出现频率
        map_ = {}  # nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1

        # 对频率排序
        # 定义一个小顶堆，大小为k
        pri_que = []  # 小顶堆

        # 用固定大小为k的小顶堆，扫面所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:  # 如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)

        # 找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒叙来输出到数组
        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result



import collections
from typing import List


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         def sift_down(arr, root, k):
#             """下沉log(k),如果新的根节点>子节点就一直下沉"""
#             val = arr[root] # 用类似插入排序的赋值交换
#             while root<<1 < k:
#                 child = root << 1
#                 # 选取左右孩子中小的与父节点交换
#                 if child|1 < k and arr[child|1][1] < arr[child][1]:
#                     child |= 1
#                 # 如果子节点<新节点,交换,如果已经有序break
#                 if arr[child][1] < val[1]:
#                     arr[root] = arr[child]
#                     root = child
#                 else:
#                     break
#             arr[root] = val
#
#         def sift_up(arr, child):
#             """上浮log(k),如果新加入的节点<父节点就一直上浮"""
#             val = arr[child]
#             while child>>1 > 0 and val[1] < arr[child>>1][1]:
#                 arr[child] = arr[child>>1]
#                 child >>= 1
#             arr[child] = val
#
#         stat = collections.Counter(nums)
#         stat = list(stat.items())
#         heap = [(0,0)]
#
#         # 构建规模为k+1的堆,新元素加入堆尾,上浮
#         for i in range(k):
#             heap.append(stat[i])
#             sift_up(heap, len(heap)-1)
#         # 维护规模为k+1的堆,如果新元素大于堆顶,入堆,并下沉
#         for i in range(k, len(stat)):
#             if stat[i][1] > heap[1][1]:
#                 heap[1] = stat[i]
#                 sift_down(heap, 1, k+1)
#         return [item[0] for item in heap[1:]]




s = Solution()
print(s.topKFrequent(nums = [1,1,1,2,2,3], k = 2))