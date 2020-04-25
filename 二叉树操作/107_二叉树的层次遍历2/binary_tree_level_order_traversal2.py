# coding: utf-8


# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其自底向上的层次遍历为：
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]


# 通过递归来解决问题
# 使用102题的解法，最后反转列表


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.ret_list(root, 0, res)
        res.reverse()
        return res

    def ret_list(self, root, level, res):
        if not root: return
        if len(res) < level + 1:
            res.append([])
        res[level].append(root.val)
        self.ret_list(root.left, level + 1, res)
        self.ret_list(root.right, level + 1, res)
