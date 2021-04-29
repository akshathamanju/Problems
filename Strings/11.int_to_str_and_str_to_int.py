'''
Integer to string
if the number to convert is a single digit
ie it is between 0-9, then we need to return the
string consisting of the single character encoding that digit

If the number has more than one digit then I need to perform the digit by digit
convertion.

the key insight is for any +ve integer x, the least significant digit in
the decimal representation is x mod 10
and the remaining digits will be x // 10
This approach will compute the digits in reverse order


ex: 423
least significant bit( x mod 10) = 3 and remaining elements( x // 10 = 42
least significant bit = 2 and remaining elements ( x // 10)= 4

The natural algorithm is to prepend the digits to the partial resulting list
as adding the digit to the beggining of the string is expensive
as we need to move all the elements
A more time efficient approach is to add each computed digit to the end
and then reverse the computed sequence



'''

class Solution:
    def int_to_str(self, num1):
        is_negative = False
        if num1 < 0:
            is_negative = True
            num1 = -num1

        res_string = []
        while True:
            res_string.append(chr(ord('0') + num1 % 10))
            num1 //= 10
            if num1 == 0:
                break

        #Adds the negative sign back if is_negative is True
        return ('-' if is_negative else '') + ''.join(reversed(res_string))
    '''
    string_to_integer:
    convert str to list of chars
    ex = "-365"
    str_list = ["-","3','6', '5']
    
    check the first_element 0f the string if it is '-' or '+'
    start the iteration from 1st index else start from oth index
    
    boundary condition will be integers range: 
    for +ve -> (2 ** 31) - 1
    for -ve -> -(2 ** 31)
    
    '''


    def string_to_integer(self, str):
        str_list = str.split()

        if not str_list:
            return 0

        num_str = str_list[0]
        sign = -1 if num_str[0] == '-' else +1
        start = 1 if num_str[0] in '-+' else 0

        num = 0
        int_boundary = -2 ** 31 if sign ==  -1 else 2**31 - 1
        for i in range(start, len(num_str)):
            ord_digit = ord(num_str[i])
            if ord_digit < 48 or ord_digit > 57:
                break

            num *= 10
            num += ord_digit - 48 # or I can do ord('0')

            if num >= int_boundary:
                num = int_boundary
                break

        return num * sign


o1 = Solution()
num1 = 365
print(o1.int_to_str(num1))
print(type(o1.int_to_str(num1)))
num1 = -365
print(o1.int_to_str(num1))
print(type(o1.int_to_str(num1)))
num1 = 3
print(o1.int_to_str(num1))
print(type(o1.int_to_str(num1)))
num1 = -8
print(o1.int_to_str(num1))
print(type(o1.int_to_str(num1)))

o2 = Solution()
str1 = "133"
print(o2.string_to_integer(str1))
print(type(o2.string_to_integer(str1)))

str1 = "-133"
print(o2.string_to_integer(str1))
print(type(o2.string_to_integer(str1)))

str1 = "0"
print(o2.string_to_integer(str1))
print(type(o2.string_to_integer(str1)))

str1 = ""
print(o2.string_to_integer(str1))
print(type(o2.string_to_integer(str1)))