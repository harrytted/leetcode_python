# coding: utf-8


# 有多个整数闭区间，区间之间可能存在重叠，请合并区间，减少区间数。
# 如 [[1,3],[6,10],[2,4],[7,9],[11,12]]
# 合并后：[[1,4],[6,12]]


# def merge_list(alist):
#     if not alist:
#         return
#     ori = []
#     for a in alist:
#         ori.append(a[0])
#         ori.append(a[1])
#     sorted(ori)
#     ori = [1,2,3,4,6,7,9,10,11,12]
#     for i in ori:


# 1、实现一个函数完成类似下面规则的字符串转化
# 输入：AABBBCADDEEF
# 输出：A2B3CAD2E2F

from collections import OrderedDict


def fn_str(str1):
    if not str1: return
    ret = ''
    len_str = len(str1)
    str_dict = OrderedDict()
    for i in range(len_str - 1):
        count = 1
        for j in range(i + 1, len_str):
            if str1[i] != str1[j]:
                break
            else:
                count += 1
        if str1[i] not in str_dict.keys():
            str_dict[str1[i]] = count
    for k, v in str_dict.items():
        ret += k + str(v) if v != 1 else k
    return ret


s = 'AABBBCADDEEFAA'
print(fn_str(s))


def fn_str(str1):
    if not str1: return
    ret = ''
    i = 0
    for s in str1:
        if not ret or ret[-1] != s:
            if i > 0:
                ret += str(i+1)
                i = 0
            ret += s
        else:
            i += 1
    return ret


a = []
while not a:
    print('ss')
s = 'AABBBCADDEEFAA'
print(fn_str(s))
print('pp')

if __name__ == '__main__':
    sum = 0
    print(a)
    print('pp')
