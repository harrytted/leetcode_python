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
        """
        迭代
        先将根结点压入栈，然后定义一个辅助结点 head
        while 循环的条件是栈不为空
        在循环中，首先将栈顶结点t取出来
        如果栈顶结点没有左右子结点，或者其左子结点是 head，或者其右子结点是 head 的情况下。我们将栈顶结点值加入结果 res 中，并将栈顶元素移出栈，然后将 head 指向栈顶元素
        否则的话就看如果右子结点不为空，将其加入栈
        再看左子结点不为空的话，就加入栈
        :param root:
        :return:
        """
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

