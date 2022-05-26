from typing import List


class Solution:
    # brute force solution
    # time complexity: O(n^2)
    # space complexity: O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size - 1):
            j = i + 1
            for j in range(j, size):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # hash map solution
    # time complexity: O(n)
    # space complexity: O(n)
    def optimizedTwoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                return [seen[remaining], i]

            seen[num] = i


if __name__ == '__main__':
    nums = [4, 3, 2, 1]
    target = 4
    solution = Solution().optimizedTwoSum(nums, target)
    print(solution)
