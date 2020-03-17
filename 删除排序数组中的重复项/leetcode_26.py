# coding: utf-8

# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

# 给定 nums = [0,0,1,1,1,2,2,3,3,4],
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
# 不需要考虑数组中超出新长度后面的元素。

# 解题思路
# 使用快慢指针来记录遍历的坐标。
# 开始时这两个指针都指向第一个数字
# 如果两个指针指的数字相同，则快指针向前走一步
# 如果不同，则两个指针都向前走一步
# 当快指针走完整个数组后，慢指针当前的坐标加 1 就是数组中不同数字的个数


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            slow = 0
            for fast in range(1, len(nums)):
                if nums[fast] != nums[slow]:
                    slow += 1
                    nums[slow] = nums[fast]
            return slow + 1
        else:
            return 0
