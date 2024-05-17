# 题目：二叉树的层序遍历
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
# 输入：root = [1]
# 输出：[[1]]
# 输入：root = []
# 输出：[]

def levelOrder(root):
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        size = len(queue)
        tmp = []
        for _ in range(size):
            r = queue.pop(0)
            tmp.append(r.val)
            if r.left:
                queue.append(r.left)
            if r.right:
                queue.append(r.right)
        res.append(tmp)
    return res
