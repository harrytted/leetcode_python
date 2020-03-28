# coding: utf-8


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class BST(object):

    def __init__(self, val):
        self.val = val
        self.right, self.left = None, None

    def bian_li(self, root, target):
        if root.val == target:
            pass
        if root.val < target:
            self.bian_li(root.right, target)
        if root.val > target:
            self.bian_li(root.left, target)

    def insert_val(self, root, val):
        if root.val is None:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insert_val(root.right, val)
        if root.val > val:
            self.insert_val(root.left, val)
        return root

    def del_val(self, root, val):
        if root.val == val:
            pass
        if root.val < val:
            root.right = self.del_val(root.right, val)
        elif root.val > val:
            root.left = self.del_val(root.left, val)
        return root
