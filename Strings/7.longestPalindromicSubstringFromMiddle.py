'''
s = 'babad'
o/p : 'bab' or 'aba' -> odd len

s = 'cbbd'
o/p: 'bb'-> even len

'''
class Solution:
    def longestPalindrome(self, s):

        if not s:
            return ""

        N = len(s)
        res = ''

        def longestPalindromic_substring_from_middle(left, right):
            while left >= 0 and right < N and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]
        for i in range(N):
            #babab
            oddMiddle = longestPalindromic_substring_from_middle(i, i)
            #abba, cbbd
            evenMiddle = longestPalindromic_substring_from_middle(i, i+1)

            if len(oddMiddle) > len(res):
                res = oddMiddle
            if len(evenMiddle) > len(res):
                res = evenMiddle
        return  res

o1 = Solution()
s = "babad"
print(o1.longestPalindrome(s))

s1 = "cbbd"
print(o1.longestPalindrome(s1))

s2 = "a"
print(o1.longestPalindrome(s2))

s3 = "ac"
print(o1.longestPalindrome(s3))