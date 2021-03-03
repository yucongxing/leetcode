from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increase, decrease = True, True
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                decrease = False
            if A[i] < A[i - 1]:
                increase = False
            if not (increase or decrease):
                return False
            
        return increase or decrease


if __name__ == "__main__":
    s = Solution()
    print(s.isMonotonic([1, 2, 2, 3]))
