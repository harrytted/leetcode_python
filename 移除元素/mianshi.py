

class Solution:
    # array 二维列表
    def Find(self, target, array):
        rows = len(array) - 1
        cols = len(array[0]) - 1
        i = rows
        j = 0
        while j <= cols and i > 0:
            if target < array[i][j]:
                i -= 1
            elif target > array[i][j]:
                j += 1
            else:
                return True
        return False


def isPrime(n):
    if n < 2:
        return "no prime"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def nthPrime(n):
    numberOfPrimes = 0
    prime = 1

    while numberOfPrimes < n:
        prime += 1
        if isPrime(prime):
            numberOfPrimes += 1
    return prime


print(nthPrime(10001))


if __name__ == '__main__':
    sum = 0
    for i in range(1, 88):
        sum += i
    print(sum)
    da = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    target = 1
    a = Solution().Find(target, da)
    print(a)
    print('pp')
