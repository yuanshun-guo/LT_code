def sort_way1(nums):
    '''
    :param nums -- list:
    :return:
    '''
    nums.sort()
    return nums

def sort_way2(nums):
    sorted(nums)
    return nums

print(sort_way2([2,6,3,9,4]))