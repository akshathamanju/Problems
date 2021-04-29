class Solution:
    def shortestToChar(self, s, c) :
        count = 0
        res = []
        for i in reversed(range(len(s))):
            if s[i] != c:
                count += 1
                #print(count, s[i])
                res.append(count)
            # print(res)
            else:
                count = 0
                res.append(count)

        return res[::-1]

o1 = Solution()
s = "loveleetcode"
c = "e"
print(o1.shortestToChar(s,c))

s = "loveleetcod"
c = "e"
print(o1.shortestToChar(s,c))