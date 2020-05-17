# coding: utf-8
# 给定一个二叉树，找出其最小深度。
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 说明: 叶子节点是指没有子节点的节点。
# 示例:
#
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回最小深度2


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return 1+self.minDepth(root.right)

        if root.right is None:
            return 1 + self.minDepth(root.left)
        return min(1+self.minDepth(root.left), 1+self.minDepth(root.right))