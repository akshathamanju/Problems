class Solution:
    def groupAnagrams(self, strs):
        my_dict = {}
        for word in strs:
            sortedWord = "".join(sorted(word))

            if sortedWord not in my_dict:
                my_dict[sortedWord] = [word]
            else:
                my_dict[sortedWord].append(word)
        result = []
        for item in my_dict.values():
            result.append(item)
        return result

o1 = Solution()
in1 = ["eat","tea","tan","ate","nat","bat"]
print(o1.groupAnagrams(in1))
in1 = [""]
print(o1.groupAnagrams(in1))
in1 = ["a"]
print(o1.groupAnagrams(in1))
