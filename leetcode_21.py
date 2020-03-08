# coding: utf-8


# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 解题思路
# 用递归实现，新链表也不需要构造新节点，我们下面列举递归三个要素
# 终止条件：两条链表分别名为 l1 和 l2，当 l1 为空或 l2 为空时结束
# 返回值：每一层调用都返回排序好的链表头
# 本级递归内容：如果 l1 的 val 值更小，则将 l1.next 与排序好的链表头相接，l2 同理
# O(m+n)O(m+n)，mm 为 l1的长度，nn 为 l2 的长度

# 时间复杂度：O(n + m)O(n+m)。 因为每次调用递归都会去掉 l1 或者 l2 的头元素（直到至少有一个链表为空），函数 mergeTwoList 中只会遍历每个元素一次。所以，时间复杂度与合并后的链表长度为线性关系。


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


