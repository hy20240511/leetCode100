# 题目：除自身以外数组的乘积
# 给你一个整数数组nums，返回数组answer ，其中answer[i]等于nums中除nums[i]之外其余各元素的乘积 。
# 题目数据保证数组nums之中任意元素的全部前缀元素和后缀的乘积都在32位整数范围内。不要使用除法，且在O(n)时间复杂度内完成此题。
#
# 输入: nums = [1, 2, 3, 4]
# 输出: [24, 12, 8, 6]
#
# 输入: nums = [-1, 1, 0, -3, 3]
# 输出: [0, 0, 9, 0, 0]
def productExceptSelf(nums):
    n = len(nums)
    answer = [1]*n
    l, r = [1]*n, [1]*n
    for i in range(1,n):
        l[i] = l[i-1] * nums[i-1]
    for i in reversed(range(n-1)):
        r[i] = nums[i+1] * r[i+1]
    for i in range(n):
        answer[i] = l[i] * r[i]
    return answer
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))



