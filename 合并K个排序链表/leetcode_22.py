# coding: utf-8

# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

# 输入：[1->4->5, 1->3->4, 2->6]
# 输出：1->1->2->3->4->4->5->6

# 解题思路
# 遍历所有链表，将所有节点的值放到一个数组中。
# 将这个数组排序，然后遍历所有元素得到正确顺序的值。
# 用遍历得到的值，创建一个新的有序链表。


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    @staticmethod
    def mergeKLists(lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        length = len(lists)
        if not length:
            return
        head = point = ListNode(0)
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next

        for n in sorted(nodes):
            point.next = ListNode(n)
            point = point.next
        return head.next
