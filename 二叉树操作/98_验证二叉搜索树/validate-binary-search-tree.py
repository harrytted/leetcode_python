# coding: utf-8


# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 假设一个二叉搜索树具有如下特征：
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。


# 输入:
#     2
#    / \
#   1   3
# 输出: true

# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。


# 解题思路
# 中序遍历的性质如果一个树遍历的结果是有序数组，那么他也是一个二叉查找树(BST),
# 我们只需要中序遍历，然后两两判断是否有逆序的元素对即可，如果有，则不是BST，否则即为一个BST.
# 一个结点若是在根的左子树上，那它应该小于根结点的值而大于左子树最大值；若是在根的右子树上，那它应该大于根结点的值而小于右子树最小值。
# 也就是说，每一个结点必须落在某个取值范围：
# 根结点的取值范围为（考虑某个结点为最大或最小整数的情况）：(long_min, long_max)
# 左子树的取值范围为：(current_min, root.value)
# 右子树的取值范围为：(root.value, current_max)


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_BST(root, float('-inf'), float('inf'))

    def is_BST(self, root, min, max):
        if not root:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.is_BST(root.left, min, root.val) and self.is_BST(root.right, root.val, max)
