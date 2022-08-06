class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        c = 0

        # A simple double for iteration that compares each character in each string of strs list.
        for char in range(len(min(strs))):
            for i, _ in enumerate(strs):
                if min(strs)[char] == strs[i][char]:
                    c += 1
            # If the all the character was present in every string, add it to prefix string
            if c == len(strs):
                prefix += min(strs)[char]
                c = 0
            else:
                break

        return prefix
