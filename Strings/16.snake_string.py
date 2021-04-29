class Solution:
    def snake_string(self, str1):
        result = []
        #outputs the first roe i.e s[1], s[5], s[9
        for i in range(1, len(str1), 4):
            result.append(str1[i])
        #outputs the second row, ie s[0], s[2], s[4]..
        for i in range(0, len(str1), 2):
            result.append(str1[i])
        # outputs the thrid row s[3], s[7], s[11]
        for i in range(3, len(str1), 4):
            result.append(str1[i])

        return ''.join(result)


o1 = Solution()
str1 = "Hello_World!"
print(o1.snake_string(str1))


# python solution uses slicing with right steps
def snake_string_pythonic( str2):
    return str2[1::4] + str2[::2] + str2[3::4]

str1 = "Hello_World!"
print(snake_string_pythonic(str1))