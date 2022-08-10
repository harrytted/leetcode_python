# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。


# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
# 思路：
"""
对于每层，从左上方开始以顺时针的顺序遍历所有元素。假设当前层的左上角位于(top, left)，右下角位于(bottom, right)，按照如下顺序遍历当前层的元素
1、从左到右遍历上侧元素，依次为(top, left)到(top, right)
2、从上到下遍历右侧元素，依次为(top+1, right)到(bottom, right)
3、如果left<right 且top<bottom，则从右到左遍历下侧元素，依次为 (bottom,right−1) 到 (bottom,left+1)，
以及从下到上遍历左侧元素，依次为 (bottom,left) 到 (top+1,left)。

遍历完当前层的元素之后，将left 和 top 分别增加 1，将right 和 bottom 分别减少 1，进入下一层继续遍历，直到遍历完所有元素为止。


"""
from typing import List


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows, columns = len(matrix), len(matrix[0])
        res = list()
        left, right, top, bottom = 0, columns - 1, 0, columns - 1

        while left <= right and top <= bottom:

            # 从左到右遍历上侧元素
            for column in range(left, right + 1):
                res.append(matrix[top][column])
            # 从上到下遍历右侧元素
            for row in range(top+1, bottom + 1):
                res.append(matrix[row][right])

            if left < right and top < bottom:
                # 从右到左遍历下侧元素
                for column in range(right - 1, left, -1):
                    res.append(matrix[bottom][column])

                # 从下到上遍历左侧元素
                for row in range(bottom, top, -1):
                    res.append(matrix[row][left])

            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return res

    # 看过最好的解法，只能说python大法好
    def spiralOrder_more(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            # 削头（第一层）
            res += matrix.pop(0)
            # 将剩下的逆时针转九十度，等待下次被削
            matrix = list(zip(*matrix))[::-1]
        return res