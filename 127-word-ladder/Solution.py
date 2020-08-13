from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        q = [(beginWord, 1)]
        if endWord not in wordList:
            return 0
        while q:
            node, level = q.pop(0)
            if node == endWord:
                return level
            for i in range(len(node)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    new = node[:i] + j + node[i + 1:]
                    if new in wordList:
                        q.append((new, level + 1))
                        wordList.remove(new)
        return 0
