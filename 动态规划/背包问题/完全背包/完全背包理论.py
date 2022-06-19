"""
1）完全背包和01背包问题唯一不同的地方就是，每种物品有无限件。
2）01背包和完全背包唯一不同就是体现在遍历顺序上，所以本文就不去做动规五部曲了，我们直接针对遍历顺序经行分析！

3）我们知道01背包内嵌的循环是从大到小遍历，为了保证每个物品仅被添加一次。
    而完全背包的物品是可以添加多次的，所以要从小到大去遍历，即

4）关于遍历顺序问题：
    01背包中二维dp数组的两个for遍历的先后循序是可以颠倒了，一维dp数组的两个for循环先后循序一定是先遍历物品，再遍历背包容量。
    在完全背包中，对于一维dp数组来说，其实两个for循环嵌套顺序同样无所谓！
"""


def test_complate_pack(weight, value, bag_weight):
    dp = [0] * (bag_weight + 1)

    for i in range(len(weight)):
        for j in range(weight[i], bag_weight + 1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    print(dp[bag_weight])


weight = [1, 3, 4]
value = [15, 20, 30]
bag_weight = 4
test_complate_pack(weight, value, bag_weight)
