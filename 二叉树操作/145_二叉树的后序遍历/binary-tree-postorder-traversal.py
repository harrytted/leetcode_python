# coding: utf-8
# 给定一个二叉树，返回它的 后序 遍历。
# 示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [3,2,1]
# 左右中


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)

        if left:
            res.extend(left)
        if right:
            res.extend(right)
        res.append(root.val)
        return res

    def postorderTraversal2(self, root):
        res = []
        if not res
            return res
        stack1 = []
        stack1.append(root)
        while len(stack1) > 0:
            node = stack1.pop()
            res.append(node.val)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        return res[0:0:-1]

