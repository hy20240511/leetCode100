# 题目：最长连续序列
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为O(n)的算法解决此问题。
#
# 输入：nums = [100, 4, 200, 1, 3, 2]
# 输出：4
# 解释：最长数字连续序列是[1, 2, 3, 4]。它的长度为
# 4。
#
# 输入：nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# 输出：9

def longestConsecutive(nums):
    nums_set = set(nums)
    longest_streak = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums_set:
                current_streak += 1
                current_num += 1

            longest_streak = max(longest_streak,current_streak)
    return longest_streak

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longestConsecutive(nums))