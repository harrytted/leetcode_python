# coding: utf-8
# 给定一个二叉树，原地将它展开为一个单链表。
# 例如，给定二叉树
#
#      1
#     / \
#    5   2
#  /  \   \
# 4    3   6
# 将其展开为：
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        left_node = root.left
        right_node = root.right
        root.left = None
        self.flatten(left_node)
        self.flatten(right_node)
        if left_node:
            root.right = left_node
            while left_node.right:
                left_node = left_node.right
            left_node.right = right_node