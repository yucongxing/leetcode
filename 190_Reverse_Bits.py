class Solution:
    def reverseBits(self, n: int) -> int:
        # method 1 transfer to string
        # method 2
        # method 3
        s = str(bin(n))[2:]
        s = s[::-1] + '0' * 32
        print(len(s))
        return int(s[:32], 2)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(43261596))
