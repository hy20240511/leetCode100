# 题目：翻转二叉树
# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]
# 输入：root = [2,1,3]
# 输出：[2,3,1]
# 输入：root = []
# 输出：[]

def invertTree(root):
    if not root:
        return root
    left = invertTree(root.left)
    right = invertTree(root.right)
    root.left, root.right = right, left
    return root
