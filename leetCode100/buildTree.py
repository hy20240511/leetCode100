# 题目：从前序与中序遍历序列构造二叉树
# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]
from idlelib.tree import TreeNode


def buildTree(preorder,inorder):
    def myBuildTree(preorder_left, preorder_right, inorder_left, inorder_right):
        if preorder_left > preorder_right:
            return None

        preorder_root = preorder_left
        inorder_root = index[preorder[preorder_root]]
        root = TreeNode(preorder[preorder_root])
        size_left_subtree = inorder_root - inorder_left
        root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
        root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
        return root

    n = len(preorder)
    index = {element: i for i, element in enumerate(inorder)}
    return myBuildTree(0, n - 1, 0, n - 1)