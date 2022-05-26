from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]

    # space complexity: O(1)
    def optimizedBuildArray(self, nums: List[int]) -> List[int]:
        q = len(nums)
        for i,c in enumerate(nums):
            nums[i] += q * (nums[c] % q)
        for i,_ in enumerate(nums):
            nums[i] //= q
        return nums


if __name__ == '__main__':
    nums = [0, 2, 1, 5, 3, 4]
    ans = Solution().optimizedBuildArray(nums)
    print(ans)
