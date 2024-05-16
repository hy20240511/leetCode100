# 题目：二叉树的直径
# 给你一棵二叉树的根节点，返回该树的 直径 。
# 二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
# 两节点之间路径的 长度 由它们之间边数表示。
# 输入：root = [1,2,3,4,5]
# 输出：3
# 解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
# 输入：root = [1,2]
# 输出：1

def diameterOfBinaryTree(self,root):
    self.ans = 1
    def depth(node):
        if not node:
            return 0
        l = depth(node.left)
        r = depth(node.right)
        self.ans = max(self.ans,l+r+1)
        return max(l,r)+1
    depth(root)
    return self.ans-1
