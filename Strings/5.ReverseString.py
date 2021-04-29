class Solution:
    def reverseString(self, s):
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

o1 = Solution()
input = ["h","e","l","l","o"]
print(input)
o1.reverseString(input)
print(input)

input1 =["H","a","n","n","a","h"]
print(input1)
o1.reverseString(input1)
print(input1)
