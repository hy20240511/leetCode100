# 题目：二叉树的最大深度
# 给定一个二叉树 root ，返回其最大深度。
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
# 输入：root = [3,9,20,null,null,15,7]
# 输出：3
# 输入：root = [1,null,2]
# 输出：2
#
def maxDepth(root):
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth,right_depth)+1

