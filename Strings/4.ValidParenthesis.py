
class Solution:
    def valid_paranthesis(self, brackets):
        closing = [')', ']', '}']
        stack = []
        for bracket in brackets:
            if bracket in closing:
                if stack == []:
                    return False
                top = stack.pop()
                if bracket == ')' and top != '(':
                    return False
                elif bracket == ']' and top != '[':
                    return False
                elif bracket == '}' and top != '{':
                    return False
            else:
                stack.append(bracket)
        if stack != []:
            return False
        return True

o1 = Solution()
s = "()"
print(o1.valid_paranthesis(s))
s = "()[]{}"
print(o1.valid_paranthesis(s))
s = "(]"
print((o1.valid_paranthesis(s)))
s = "([)]"
print((o1.valid_paranthesis(s)))
s = "{[]}"
print((o1.valid_paranthesis(s)))