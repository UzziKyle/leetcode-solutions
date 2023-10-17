# EASY

# first submission
# runtime: 29 ms
# memory: 16.27 MB 
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        rev = s[::-1]
        length = len(rev)
        word = []
        idx = 0
        while True:
            char = rev[idx]
            if char == ' ' and word == []:
                idx += 1
                continue

            if idx == length - 1:
                if char != ' ':
                    word.append(char)
                break 

            if char == ' ':
                break

            word.append(char)
            idx += 1

        return len(word)