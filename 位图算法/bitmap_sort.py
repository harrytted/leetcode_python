# coding: utf-8

# 输入：一个最多包含n个正整数的文件，每个数都小于n，其中n=10^7。如果在输入文件中有任何正数重复出现就是致命错误。没有其他数据与该正数相关联。
# 输出：按升序排列的输入正数的列表。
# 约束：最多有1MB的内存空间可用，有充足的磁盘存储空间可用。运行时间最多几分钟，运行时间为10秒就不需要进一步优化。

# 笨方法
# 一种解决方法是把整个文件分成 40 份，每份 250000 个整数，一个整形占 4 字节，刚好可以在 1MB 的空间里操作。
# 在第一趟遍历中，将大小为 0 至 249999 之间的任何整数都读入内存中，并对这 250000 个整数进行排序，写到输出文件中。
# 第二趟遍历排序 250000 至 499999 之间的整数，依此类推，到第 40 趟结束，我们已经完成了排序。这种排序的代价是要读取输入文件 40 次

# 思路
# 一般编程语言的 int 类型所占空间大于等于 4 字节，共 32 位。我们可以用这 32 位来表示 0 到 31 的的数字。假设有一个集合为 {0, 3, 5}，
# 在位图里表示就是 0000101001 ，这里省去了前面 22 个 0 。一个 32 位的 int 数可以表示 32 个数字。
# 假设总共有 100 个数，我们只需 (100/32)+1=4 个 int 整数就可以表示这 100 个数，0~31 储存在第 1 个 int 数，32~63 储存在第 2 个 int 数。
# 这样，存储所有数值需要的 int 个数为 10^7 / 32 = 312500, 需要总内存为312500 * 4 / 1024 / 1024 = 1.25M,
# 1M内存限制跑两趟就可以完成排序


# 位图排序实现
# 我们可以用 3 个函数来实现位图。
# 函数1：将所有的位都置为0，从而将集合初始化为空。
# 函数2：通过读入文件中的每个整数来建立集合，将每个对应的位置都置为 1。
# 函数3：检验每一位，如果该为为1，就输出对应的整数。


class BitMap(object):
    def __init__(self, maxval, bitsperword=32, shift=5, mask=0b11111):
        """
        :param maxval: 最大值
        :param bitsperword: 一个int数的位数
        :param shift: 能表示 bitsperword 需要的位数, 5 位可以表示 32 这个数
        :param mask: 能表示 bitsperword 需要的位数，用二进制表示
        """
        self.maxval = maxval
        self.bitsperword = bitsperword
        self.shift = shift
        self.mask = mask
        # 初始化位图，相当于函数1
        self.bit = [0 for i in range(1+int(maxval / bitsperword))]

    def set_bit(self, i):
        # i>>self.shift 操作等同于 i 除于 2^self.shift
        # i & self.mask 操作等同于 i 对 2^self.shift 求余
        # 1 << n 等同于 1 * 2^n
        self.bit[i >> self.shift] |= (1 << (i & self.mask))

    def get_bit_val(self, i):
        # 如果某位上有数，就返回 true
        return self.bit[i >> self.shift] & (1 << (i & self.mask))


def bitSort(lists, maxval):
    sortLists = []
    bit = BitMap(maxval)
    for val in lists:
        bit.set_bit(val)
    for i in range(maxval+1):
        if bit.get_bit_val(i):
            sortLists.append(i)
    return sortLists


if __name__ == '__main__':
    lists = [1, 5, 2, 6, 8, 10, 22, 25, 44, 29, 35, 40, 3, 4, 20, 27, 37, 39]
    print (bitSort(lists, max(lists)))