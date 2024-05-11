# 题目：移动零
# 给定一个数组nums，编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
#
# 输入: nums = [0, 1, 0, 3, 12]
# 输出: [1, 3, 12, 0, 0]
#
# 输入: nums = [0]
# 输出: [0]
def moveZeroes(nums):
    n = len(nums)
    left = right = 0
    while right < n:
        if nums[right] != 0:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
        else:
            right += 1
    return  nums

nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))
