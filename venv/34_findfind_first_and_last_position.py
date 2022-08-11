# 34. 在排序数组中查找元素的第一个和最后一个位置
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回[-1, -1]。
# 你必须设计并实现时间复杂度为O(log n)的算法解决此问题。
# 示例 1：
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 示例2：
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 示例 3：
# 输入：nums = [], target = 0
# 输出：[-1,-1]


# 思路 二分法
# 道理与找左侧边界是一样的，只是在当nums[mid] == target时，将左侧边界left向右侧收紧left = mid+1，还有while结束的边界判断条件不同。
# 如果 nums 中不存在 target 这个值，有两种情况：
#
# target比nums中的值都大，那么算法结束left == right == len(nums) and nums[right-1] != target ，此时返回-1；注意，此处为了区分是写的right-1但实际二者都是一样的，因为搜索区间左闭右开，所以最右侧需要-1避免越界。
# target比nums中的值都小，那么算法结束left == right == 0，返回-1

class Solution:

    def binarySearch(self, nums:List[int],target:int):
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right-left)//2 # 等价于(left+right)//2 防止溢出
            if nums[mid] == target:
                left = mid+1 # 相等收缩左侧边界
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid
        # target小于所有nums
        if right == 0:
            return -1
        return right-1 if nums[right-1] == target else -1
