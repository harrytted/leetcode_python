# coding: utf-8

# 给定一个二叉树，检查它是否是镜像对称的。
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。


# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3

# 解题思路
# 用递归做比较简单：一棵树是对称的等价于它的左子树和右子树两棵树是对称的，问题就转变为判断两棵树是否对称
# 均为none ，symmetric
# 左孩子，右孩子都不存在，并且值相等， symmetric
# 右子树 和 另一棵树的左子树相等，左子树 和另一颗树的右子树相等


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.symmetric(root.left, root.right)

    def symmetric(self, l1, l2):
        if not l1 or not l2:
            if not l1 and not l2:
                return True
            else:
                return False
        if l1.val == l2.val:
            return self.symmetric(l1.right, l2.left) and self.symmetric(l1.left, l2.right)
        else:
            return False
