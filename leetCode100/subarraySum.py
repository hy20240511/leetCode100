# 题目：和为K的子数组
# 给你一个整数数组nums和一个整数k ，请你统计并返回该数组中和为k的子数组的个数 。
# 子数组是数组中元素的连续非空序列。
#
# 输入：nums = [1, 1, 1], k = 2
# 输出：2
#
# 输入：nums = [1, 2, 3], k = 3
# 输出：2
import collections


def subarraySum(nums,k):
    preNums = collections.defaultdict(int)
    preNums[0] = 1
    preNum = 0
    count = 0
    for i in range(len(nums)):
        preNum += nums[i]
        count += preNums[preNum-k]
        preNums[preNum] += 1
    return  count
nums = [1, 1, 1]
nums1 = [1, 2, 3]
print(subarraySum(nums,2))
print(subarraySum(nums1,3))