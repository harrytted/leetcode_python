# coding: utf-8

# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 返回如下的二叉树：
#
#   3
#  /  \
# 9    20
#     / \
#    7  15

# 构建二叉树的问题本质上就是：
# 找到各个子树的根节点 root
# 构建该根节点的左子树
# 构建该根节点的右子树
# 一句话，看到树就要想到递归
# inorder 是 左 -> 根 -> 右
# postorder 是 左 -> 右 -> 根
# 首先pre的第一个就是整个树的root, 假设 preorder[0] = inorder[k],那么inorder的前k-1个就是树的左子树，后面部分就是树的右子树


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if postorder == inorder == []:
            return None
        # 根据后序数组的最后一个元素，就可以确定根节点
        root = TreeNode(postorder[-1])
        # 用preorder[-1]去中序数组中查找对应的元素
        k = inorder.index(postorder[-1])

        # 递归的处理前序数组的左边部分和中序数组的左边部分
        # 递归处理前序数组右边部分和中序数组右边部分
        root.left = self.buildTree(inorder[:k], postorder[:k])
        root.right = self.buildTree(inorder[k + 1:], postorder[k:-1])
        return root


if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    s = Solution()
    a = s.buildTree(inorder, postorder)
    print(a)
