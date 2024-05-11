# 题目：三数之和
# 给你一个整数数组nums ，判断是否存在三元组[nums[i], nums[j], nums[k]]
# 满足i != j、i != k且j != k ，同时还满足nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为0且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
#
# 示例
# 输入：nums = [-1, 0, 1, 2, -1, -4]
# 输出：[[-1, -1, 2], [-1, 0, 1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是[-1, 0, 1]
# 和[-1, -1, 2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
#
# 输入：nums = [0, 1, 1]
# 输出：[]
# 解释：唯一可能的三元组和不为0 。
#
# 输入：nums = [0, 0, 0]
# 输出：[[0, 0, 0]]
# 解释：唯一可能的三元组和为0 。

def threeSum(nums):
    nums.sort()
    ans = list()
    for first in range(len(nums)):
        if first > 0 and nums[first] == nums[first-1]:
            continue
        target = -nums[first]
        third = len(nums) - 1
        for second in range(first+1,len(nums)):
            if second > first + 1 and nums[second] == nums[second-1]:
                continue
            while second < third and nums[second] + nums[third] > target:
                third -= 1
            if second == third:
                break
            if nums[second] + nums[third] == target:
                ans.append([nums[first], nums[second], nums[third]])

    return ans
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))

