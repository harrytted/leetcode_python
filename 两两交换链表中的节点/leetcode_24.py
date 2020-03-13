# coding: utf-8

# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 给定 1->2->3->4, 应该返回 2->1->4->3.

# 解题思路
# 从链表的头节点 head 开始递归。
# 每次递归都负责交换一对节点。由 firstNode 和 secondNode 表示要交换的两个节点。
# 下一次递归则是传递的是下一对需要交换的节点。若链表中还有节点，则继续递归。
# 交换了两个节点以后，返回 secondNode，因为它是交换后的新头。
# 在所有节点交换完成以后，我们返回交换后的头，实际上是原始链表的第二个节点


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        next_head = head.next
        head.next = self.swapPairs(next_head.next)
        next_head.next = head
        return next_head