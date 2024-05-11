# 题目：接雨水
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 示例：
# 输入：height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# 输出：6
# 解释：上面是由数组[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# 表示的高度图，在这种情况下，可以接6个单位的雨水（蓝色部分表示雨水）。
#
# 输入：height = [4, 2, 0, 3, 2, 5]
# 输出：9

def trap(height):
    left, right = 0 ,len(height)-1
    leftMax = rightMax = 0
    ans = 0
    while left < right:
        leftMax = max(leftMax,height[left])
        rightMax = max(rightMax,height[right])
        if height[left] < height[right]:
            ans += leftMax-height[left]
            left += 1
        else:
            ans += rightMax-height[right]
            right -= 1
    return ans
height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height2 = [4, 2, 0, 3, 2, 5]
print(trap(height1))
print(trap(height2))
