class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_arr = version1.split(".")
        version2_arr = version2.split(".")
        m = len(version1_arr)
        n = len(version2_arr)
        i = 0
        while i < m and i < n:
            if int(version1_arr[i]) > int(version2_arr[i]):
                return 1
            elif int(version1_arr[i]) < int(version2_arr[i]):
                return -1
            else:
                i += 1
                continue
        if i < m:
            for j in range(i, m):
                if int(version1_arr[j]) != 0:
                    return 1
        if i < n:
            for j in range(i, n):
                if int(version2_arr[j]) != 0:
                    return -1
        return 0


