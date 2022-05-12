"""hard"""
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # defaultdic(list) 是为了方便直接append
        from collections import defaultdict
        tickets_dict = defaultdict(list)
        for key, value in tickets:
            tickets_dict[key].append(value)

        result = ['JFK']
        self.backtracking(tickets, 'JFK', result, tickets_dict)
        return result

    def backtracking(self, ticket: List[List[str]], start_point: str, result: List[str],
                     tickets_dict: {str: List[str]}) -> bool:

        # 终止条件
        if len(result) == len(ticket) + 1:
            return True
        tickets_dict[start_point].sort()
        for _ in tickets_dict[start_point]:
            # 必须及时删除，避免出现死循环
            end_point = tickets_dict[start_point].pop(0)
            result.append(end_point)
            # 只要找到一个就可以返回了
            if self.backtracking(tickets_dict, end_point, result, tickets_dict):
                return True
            result.pop()
            tickets_dict[start_point].append(end_point)
