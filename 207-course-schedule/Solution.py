from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = set()
        for pre in prerequisites:
            graph[pre[0]].add(pre[1])
        removed = {n for n, adjs in graph.items() if len(adjs) == 0}
        while removed:
            for n in removed:
                del graph[n]
            tmp = set()
            for n, adjs in graph.items():
                graph[n] = adjs - removed
                if len(graph[n]) == 0:
                    tmp.add(n)
            removed = tmp
        return len(graph) == 0
