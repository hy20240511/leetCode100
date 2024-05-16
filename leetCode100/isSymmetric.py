# 题目：对称二叉树
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false

def isSymmetric(root):
    if not root:
        return True

    def dfs(left, right):
        if not (left or right):
            return True
        if not (left and right):
            return False
        if left.val != right.val:
            return False
        return dfs(left.left, right.right) and dfs(left.right, right.left)

    return dfs(root.left, root.right)