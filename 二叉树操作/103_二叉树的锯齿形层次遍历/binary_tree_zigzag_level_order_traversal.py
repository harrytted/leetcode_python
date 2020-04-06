# coding: utf-8

# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回锯齿形层次遍历如下：
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


# 解题思路
# 建立一个queue
# 先把根节点放进去，这时候找根节点的左右两个子节点
# 去掉根节点，此时queue里的元素就是下一层的所有节点
# 循环遍历，将结果存到一个一维向量里
# 遍历完之后再把这个一维向量存到二维向量里
# 如果该层为偶数层，则reverse翻转一下
# 以此类推，可以完成层序遍历


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, cur_level, level_count = [], [root], 0
        while cur_level:
            next_level, tmp_res = [], []
            for node in cur_level:
                tmp_res.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if level_count % 2 == 0:
                res.append(tmp_res)
            else:
                tmp_res.reverse()
                res.append(tmp_res)
            level_count += 1
            cur_level = next_level

        return res

