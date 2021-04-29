'''
The ord() function returns the number representing the unicode code of a specified character.

we iterate through each char from left to right considering the index as 0 to len(string) => num

we multiply the 26 to each if the characters and add the value for each alphabet

the we return the number

A = 1
AA
= 0 * 26 + 1
= 1       -> A
1 * 26 = 26  -> AA
26 + 1 = 27

AB = 1 * 28 = 28

ZY
num = 0
for Z
num = num * 26 = 0
num += 26 - 1 + 1
num = 26

for Y
num = num * 26 = 26 * 26 = 676
num += 26 - 1 + 1  = (676 + 26+ -1 +1)
num = 701

Time: O(n) -> need to traverse all the elements
space O(1)
'''


class Solution:
    def titleToNumber(self, s: str) -> int:
        num = 0
        for c in s:
            num *= 26
            num += ord(c) - ord('A') + 1

        return num

o1 = Solution()
str1 = 'A'
print(o1.titleToNumber(str1))

str1 = 'AA'
print(o1.titleToNumber(str1))

str1 = 'AZ'
print(o1.titleToNumber(str1))

str1 = 'ZZ'
print(o1.titleToNumber(str1))
