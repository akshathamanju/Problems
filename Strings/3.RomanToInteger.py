class Solution:
    def romanToInteger(self, s):
        my_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total_value = 0
        curr = 0
        prev = 0

        for i in range(len(s)):
            #print('prev', prev, 'curr', curr)

            curr = my_dict[s[i]]
            if curr > prev:
                total_value = total_value + curr - (2*prev)
            else:
                total_value += curr
                print('prev', prev, 'curr', curr)
            prev = curr
        return total_value

o1 = Solution()
s = "III"
print(o1.romanToInteger(s))

s = "IV"
print(o1.romanToInteger(s))
s = "IX"
print(o1.romanToInteger(s))
s = "LVIII"
print(o1.romanToInteger(s))
s = "MCMXCIV"
print(o1.romanToInteger(s))