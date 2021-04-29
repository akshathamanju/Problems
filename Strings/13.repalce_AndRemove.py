'''
1. Replace each 'a' by 2d's
2. Delete each entry containing b

arr1 = ['a', 'c', 'd','b','b','c','a']



'''
class Solution:
    def replace_and_remove(self, size, str1):
        #forward iteration, remove b's and count the number of a's
        write_index = 0
        a_count = 0
        for i in range(size):


            if str1[i] != 'b':
                str1[write_index] = str1[i]
                write_index += 1
            if str1[i] == 'a':
                a_count += 1
        print(str1)
        #backward iteration: replace a's with dd's starting from the end
        cur_idx = write_index - 1
        write_index += a_count - 1
        final_size = write_index + 1
        while cur_idx >= 0:
            if str1[cur_idx] == 'a':
                str1[write_index - 1 : write_index + 1] = "dd"
                write_index -= 2
            else:
                str1[write_index] = str1[cur_idx]
                write_index -= 1
            cur_idx -= 1
        return str1

o1 = Solution()
arr1 = ['a', 'c', 'd','b','b','c','a']
print(o1.replace_and_remove(len(arr1), arr1))

arr1 = ['a', 'a', 'a']
print(o1.replace_and_remove(len(arr1), arr1))

arr1 = ['b', 'a', 'a']
print(o1.replace_and_remove(len(arr1), arr1))

arr1 = ['b', 'b', 'b']
print(o1.replace_and_remove(len(arr1), arr1))