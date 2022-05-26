from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            runningSum.append(total)

        return runningSum


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    ans = Solution().runningSum(nums)
    print(ans)
