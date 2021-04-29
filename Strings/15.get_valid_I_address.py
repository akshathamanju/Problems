class Solution():
    def get_valid_IP_address(self, str1):
        def is_valid_part(str1):
            return len(str1) == 1 or (str1[0] != '0' and int(str1) <= 255)

        result, parts = [], [''] * 4
        for i in range(1, min(4, len(str1))):
            parts[0] = str1[:i]
            if is_valid_part(parts[0]):
                for j in range(1, min(len(str1) - i, 4)):
                    parts[1] = str1[i: i + j]
                    if is_valid_part(parts[1]):
                        for k in range(1, min(len(str1) - i - j, 4)):
                            parts[2], parts[3] = str1[ i + j: i+ j + k], str1[i + j + k:]
                            if is_valid_part((parts[2]) and is_valid_part(parts[3])):
                                result.append('.'.join(parts))


        return result

o1 = Solution()
str1 = "19216811"
print(o1.get_valid_IP_address(str1))