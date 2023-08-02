"""
给定一个含有 n 个正整数的数组和一个正整数 target。
找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，
并返回其长度。如果不存在符合条件的子数组，返回 0 。

示例 1：
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：
输入：target = 4, nums = [1,4,4]
输出：1
示例 3：
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0
        nums_sum = 0   # 子序列的数值之和
        length = len(nums)
        ans = length + 1   # 返回的子序列的长度
        while end < length:
            nums_sum += nums[end]
            while nums_sum >= target:
                ans = min(ans, end - start + 1)
                nums_sum -= nums[start]
                start += 1
            end += 1

        return 0 if ans == length + 1 else ans


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    res = Solution().minSubArrayLen(target, nums)
    assert 2 == res