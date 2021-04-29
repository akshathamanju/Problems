class Sollution:
    def reverse_words(self, s):
        character_reverse(s, 0 , len(s)-1)
        current_word_start_index = 0

        for i in range(len(s) + 1):
            if (i == len(s)) or (s[i] == " "):
                character_reverse(s, current_word_start_index, i-1)
                current_word_start_index = i+1


def character_reverse(words, left, right):
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1


o1 = Sollution()
input1 = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
o1.reverse_words(input1)
print(input1)

input2 = [""]
o1.reverse_words(input2)
print(input2)