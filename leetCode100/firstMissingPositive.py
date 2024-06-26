# 题目：缺失的第一个正数
# 给你一个未排序的整数数组nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为O(n)并且只使用常数级别额外空间的解决方案。
#
# 输入：nums = [1, 2, 0]
# 输出：3
#
# 输入：nums = [3, 4, -1, 1]
# 输出：2
#
# 输入：nums = [7, 8, 9, 11, 12]
# 输出：1
def firstMissingPositive(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n+1
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num-1] = -abs(nums[num-1])
    for i in range(n):
        if nums[i] >= 0:
            return i+1
    return n+1

nums = [7, 8, 9, 11, 12]
print(firstMissingPositive(nums))