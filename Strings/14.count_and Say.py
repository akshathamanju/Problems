'''
Idea here is keep track of the first letter in the sequence and count consecutive occurances.
Once you encounter a new letter you add the previous count and letter to the chain.
Repeat n-1 times (since we seeded the initial '1' case). We always update temp after the inner loop
since we will never have already added the last sequence.

Time Complexity: \mathcal{O}(2^n)
where n is the index of the desired sequence.
First of all, we would invoke the function nextSequence() n−1 times to get the desired sequence.
For each invocation of the function, we would scan the current sequence whose length is difficult to determine though.
Let us image in the worst scenario where any two adjacent digit in the sequence are not identical,\
then its next sequence would double the length, rather than having a reduced length. As a result, we could assume
that in the worst case, the length of the sequence would grow exponentially.
As a result, the overall time complexity of the algorithm would be (2^n).
Space Complexity: (O(2^{n-1})−1)
Within each invocation of the nextSequence() function, we are using a container to keep the result of the next sequence.
The memory consumption of the container is proportional to the length of the sequence that the function needs to process, i.e 2^{n-1}
Though we were applying the recursion function, which typically incurs some additional memory consumption in call stack.
In our case though, the recursion is implemented in the form of tail recursion, and we assume that the compiler
could optimize its execution which would not incur additional memory consumption.
One could also easily replace the recursion with the iteration in this case.
As a result, the overall space complexity of the algorithm would be dominated by the space needed to hold the final sequence, i.e. {O}({2^{n-1}})
'''


class Solution:
    def countAndSay(self, n: int) -> str:

        # The first char of our result is 1 so initilize the result
        s = '1'

        # As we have taken care of case 1 with n == 1 we start from 2
        while n > 1:

            i = 0
            # create new string every iteration and assign it to our res
            newString = ''
            while i < len(s):
                # As we already included the first character so count = 1
                count = 1
                # Check if the prev char is same as next and keep count
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                # Finally make the new string
                newString += str(count) + s[i]
                i += 1
            # Assign the newly made string for next iteration to s
            s = newString
            n -= 1
        return s

o1 = Solution()
Input = 1
#Output: "1"
#Explanation: This is the base case.
print(o1.countAndSay(Input))

Input = 4
'''Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
'''
print(o1.countAndSay(Input))