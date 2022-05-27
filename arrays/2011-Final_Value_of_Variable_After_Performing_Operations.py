from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for operation in operations:
            if '--' in operation:
                X -= 1
            else:
                X += 1
        return X


if __name__ == '__main__':
    operations = ["--X", "X++", "X++"]
    X = Solution().finalValueAfterOperations(operations)
    print(X)
