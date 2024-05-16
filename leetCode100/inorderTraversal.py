# 题目：二叉树的中序遍历
# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
# 输入：root = []
# 输出：[]
# 输入：root = [1]
# 输出：[1]

def inorderTraversal(self,root):
    res = []
    def dfs(root):
        if not root:
            return
        dfs(root.left)
        res.append(root.val)
        dfs(root.right)
    dfs(root)
    return res