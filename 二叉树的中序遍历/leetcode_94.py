# coding: utf-8

# 给定一个二叉树，返回它的中序遍历。

# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,3,2]

# 解题思路
# 递归
# 判断当前节点(根节点)是否为 null ，是则返回空vector，
# 否则先返回当前节点的值，然后对当前节点的左节点递归，
# 最后对当前节点的右节点递归。
# 递归时对返回结果的处理方式不同可进一步细分为遍历和分治两种方法


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        if root.left:
            res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        if root.right:
            res.extend(self.inorderTraversal(root.right))
        return res


