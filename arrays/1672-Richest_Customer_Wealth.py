from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return sum(max(accounts, key=sum))


if __name__ == '__main__':
    accounts = [[1, 5], [7, 3], [3, 5]]
    ans = Solution().maximumWealth(accounts)
    print(ans)
