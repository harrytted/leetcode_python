# coding: utf-8


# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素

# 给定 nums = [0,1,2,2,3,0,4,2], val = 2,
# 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

# 解题思路
# 使用两根指针从前往后依次遍历，一根指针遍历数组，另一根指针则指向数组当前不含给定值的索引。
# 遍历时索引处的值不等于给定值则递增1，否则继续遍历，直至遍历结束，返回的索引值恰好是原地替
# 换后的数组（不含给定值）的长度

class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        if not nums:
            return
        ret = []
        for num in nums:
            if num != val:
                nums[left] = num
                left += 1
                ret.append(num)
        return left


data = [3, 2, 2, 3]
da = 3
s = Solution()
s.removeElement(nums=data, val=da)
