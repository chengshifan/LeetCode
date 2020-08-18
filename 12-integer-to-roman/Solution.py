class Solution:
    res = ''

    def intToRoman(self, num: int) -> str:

        dictionary = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                      500: 'D', 900: 'CM', 1000: 'M'}

        def helper(target, mapping):
            if target <= 0:
                return
            else:
                key = 1
                for k, v in mapping.items():
                    if key <= k <= target:
                        key = k
                        continue
                self.res += mapping[key]
                helper(target - key, mapping)

        helper(num, dictionary)
        return self.res
