class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
        return True

o1 = Solution()
str1 = "A man, a plan, a canal: Panama"
print(o1.isPalindrome(str1))

str1 = "Ray a Ray"
print(o1.isPalindrome(str1))

str1 = "Able was I, ere I saw elba"
print(o1.isPalindrome(str1))

# palindromic
def palindromic(str1):
    return all(str1[i] == str1[~i] for i in range(len(str1) // 2))

str1 = "abba"
print(palindromic(str1))
str1 = "abcba"
print(palindromic(str1))
str1 = "ba"
print(palindromic(str1))