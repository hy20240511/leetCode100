# 题目：验证二叉搜索树
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
# 有效 二叉搜索树定义如下：
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 输入：root = [2,1,3]
# 输出：true
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false

def isValidBST(root):
    def helper(node,lower = float('-inf'),upper = float('inf')):
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        if not helper(node.left,lower,val):
            return False
        if not helper(node.right,val,upper):
            return False
        return True
    return helper(root)

