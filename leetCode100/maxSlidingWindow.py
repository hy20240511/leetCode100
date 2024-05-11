# 题目：滑动窗口最大值
# 给你一个整数数组nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的k个数字。滑动窗口每次只向右移动一位。
# 返回滑动窗口中的最大值 。
#
# 输入：nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
# 输出：[3, 3, 5, 5, 6, 7]
#
# 输入：nums = [1], k = 1
# 输出：[1]
import heapq


def maxSlidingWindow(nums,k):
    n = len(nums)
    q = [(-nums[i],i) for i in range(k)]
    heapq.heapify(q)
    ans = [-q[0][0]]
    for i in range(k,n):
        heapq.heappush(q,(-nums[i],i))
        while q[0][1] <= i - k:
            heapq.heappop(q)
        ans.append(-q[0][0])
    return ans
nums = [1, 3, -1, -3, 5, 3, 6, 7]
print(maxSlidingWindow(nums,3))