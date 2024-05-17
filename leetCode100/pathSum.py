# 题目:路径总和III
# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# 输出：3
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：3

def pathSum(root,targetSum):
    def rootSum(root, targetSum):
        if root is None:
            return 0

        ret = 0
        if root.val == targetSum:
            ret += 1
        ret += rootSum(root.left, targetSum - root.val)
        ret += rootSum(root.right, targetSum - root.val)
        return ret

    if root is None:
        return 0
    ret = rootSum(root, targetSum)
    ret += pathSum(root.left, targetSum)
    ret += pathSum(root.right, targetSum)
    return ret
