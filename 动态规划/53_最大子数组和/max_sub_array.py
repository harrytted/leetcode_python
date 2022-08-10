# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组 是数组中的一个连续部分。
#
# 示例 1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组[4,-1,2,1] 的和最大，为6 。
# 示例 2：
# 输入：nums = [1]
# 输出：1
# 示例 3：
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#
# 提示:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
#
# 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
from typing import List

# 思路
# 动态规划的是首先对数组进行遍历，当前最大连续子序列和为 sum，结果为 res
# 如果 sum > 0，则说明 sum 对结果有增益效果，则 sum 保留并加上当前遍历数字
# 如果 sum <= 0，则说明 sum 对结果无增益效果，需要舍弃，则 sum 直接更新为当前遍历数字
# 每次比较 sum 和 res的大小，将最大值置为res，遍历结束返回结果
# 时间复杂度：O(n)O(n)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        res = nums[0]
        for num in nums:
            if sum > 0:
                sum += num
            else:
                sum = num
            res = max(sum, res)
        return res

    def maxSubArray_2(self, nums: List[int]) -> int:
        len_nums = len(nums)
        dp = [None] * len_nums
        dp[0] = nums[0]
        max_val = nums[0]
        for i in range(1, len_nums):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            if max_val < dp[i]:
                max_val = dp[i]
        return max_val