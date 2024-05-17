# 题目：二叉树的最大路径和
# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
# 路径和 是路径中各节点值的总和。
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
# 输入：root = [1,2,3]
# 输出：6
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42

def __init__(self):
    self.maxSum = float("-inf")
def maxPathSum(self,root):
    def maxGain(node):
        if not node:
            return 0

        leftGain = max(maxGain(node.left), 0)
        rightGain = max(maxGain(node.right), 0)
        priceNewpath = node.val + leftGain + rightGain
        self.maxSum = max(self.maxSum, priceNewpath)
        return node.val + max(leftGain, rightGain)

    maxGain(root)
    return self.maxSum
