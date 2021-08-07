from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def next(cur : int) -> int:
            return (cur + nums[cur]) % n
        for i in range(n):
            if nums[i] == 0:
                continue
            slow, fast = i, next(i)
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next(fast)]:
                if slow == fast:
                    if slow != next(slow):
                        return True
                    else:
                        break
                slow = next(slow)
                fast = next(next(fast))
            add = i
            while nums[add] * nums[next(add)] > 0:
                tmp = add
                add = next(add)
                nums[tmp] = 0
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.circularArrayLoop([2,-1,1,2,2]))
