# coding: utf-8

# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# 解题思路
# 分治思路
# count[n], count[n] 表示到正整数 i 为止的二叉搜索树个数。
# 容易得到 count[1] = 1, 根节点为1，count[2] = 2, 根节点可为1或者2。
# 那么count[3] 的根节点自然可为1，2，3
# 以 i 作为根节点，由基本的排列组合知识可知，其唯一 BST 个数为左子树的 BST
# 个数乘上右子树的 BST 个数。故对于 i 来说，其左子树由[0, i - 1]构成，
# 唯一的 BST 个数为count[i - 1], 右子树由[i + 1, n] 构成


class Solution(object):
    def numTrees(self, n):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if n < 0:
            return -1
        count = [0] * (n+1)
        count[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                count[i] += count[j] * count[i-j-1]
        return count[n]
