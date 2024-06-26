# 题目：最大子数组和
# 给你一个整数数组nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组是数组中的一个连续部分。
#
# 输入：nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 输出：6
# 解释：连续子数组[4, -1, 2, 1]的和最大，为6 。
#
# 输入：nums = [1]
# 输出：1
#
# 输入：nums = [5, 4, -1, 7, 8]
# 输出：23

def maxSubArray(nums):
    for i in range(1,len(nums)):
        nums[i] = max(nums[i-1]+nums[i],nums[i])
    return max(nums)
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))