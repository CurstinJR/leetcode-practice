from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(sen.split(sep=' ')) for sen in sentences)

    def optimizedMostWordsFound(self, sentences: List[str]) -> int:
        return max(sen.count(" ") for sen in sentences) + 1


if __name__ == '__main__':
    sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    ans = Solution().optimizedMostWordsFound(sentences)
    print(ans)
