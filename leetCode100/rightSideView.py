# 题目：二叉树的右视图
# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
# 输入: [1,null,3]
# 输出: [1,3]
# 输入: []
# 输出: []

def rightSideView(root):
    ans = []

    def dfs(node, depth):
        if node is None:
            return
        if depth == len(ans):
            ans.append(node.val)
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)
    return ans