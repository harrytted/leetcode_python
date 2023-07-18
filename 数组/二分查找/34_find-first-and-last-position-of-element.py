"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：
输入：nums = [], target = 0
输出：[-1,-1]

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109
"""
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def get_right_border(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            right_border = -2
            while left <= right:
                middle = (left + right) // 2
                if target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
                    right_border = middle
            return right_border

        def get_left_border(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            left_border = -2
            while left <= right:
                middle = (left + right) // 2
                if target < nums[middle]:
                    right = middle - 1
                    left_border = right
                else:
                    left = middle + 1
            return left_border

        leftBoder = get_left_border(nums, target)
        rightBoder = get_right_border(nums, target)
        # 情况一
        if leftBoder == -2 or rightBoder == -2: return [-1, -1]
        # 情况三
        if rightBoder - leftBoder > 1: return [leftBoder + 1, rightBoder - 1]
        # 情况二
        return [-1, -1]
