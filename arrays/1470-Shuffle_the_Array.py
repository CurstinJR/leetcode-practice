from typing import List


class Solution:
    # time complexity: O(n^2) because of 2 for loops
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffle = []
        for i in range(0, n):
            for j in range(i, len(nums), n):
                shuffle.append(nums[j])
        return shuffle

    # time complexity: O(n)
    def alternativeShuffle(self, nums: List[int], n: int) -> List[int]:
        lst = []
        for i in range(n):
            lst.append(nums[i])
            lst.append(nums[i + n])
        return lst


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 5
    ans = Solution().alternativeShuffle(nums, n)
    print(ans)
