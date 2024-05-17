# 题目：将有序数组转换为二叉搜索树
# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡二叉搜索树。
# 输入：nums = [-10,-3,0,5,9]
# 输出：[0,-3,9,-10,null,5]
# 输入：nums = [1,3]
# 输出：[3,1]
from idlelib.tree import TreeNode


def sortedArrayToBST(nums):
    def helper(left, right):
        if left > right:
            return None

        mid = (left + right) // 2

        root = TreeNode(nums[mid])

        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root

    return helper(0, len(nums) - 1)
