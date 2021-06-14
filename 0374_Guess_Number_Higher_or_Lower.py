class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            middle = (l + r) >> 1
            re = guess(middle)
            if re == 0:
                return middle
            elif re == -1:
                r = middle - 1
            else:
                l = middle + 1
        return l
