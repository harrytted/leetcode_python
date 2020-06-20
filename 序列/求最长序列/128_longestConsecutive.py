# coding: utf-8

# 给定一个未排序的整数数组，找出最长连续序列的长度。
# 要求算法的时间复杂度为 O(n)。
# 示例:
#
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

# 动态规划
# 用哈希表存储每个端点值对应连续区间的长度
# 若数已在哈希表中：跳过不做处理
# 若是新数加入：
# 取出其左右相邻数已有的连续区间长度 left 和 right
# 计算当前数的区间长度为：cur_length = left + right + 1
# 根据 cur_length 更新最大长度 max_length 的值
# 更新区间两端点的长度值


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_dict = {}
        max_length = 0
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num-1, 0)
                right = hash_dict.get(num+1, 0)
                cur_length = 1+left+right
                if cur_length > max_length:
                    max_length = cur_length

                hash_dict[num] = cur_length
                hash_dict[num-left] = cur_length
                hash_dict[num+right] = cur_length
        return max_length
