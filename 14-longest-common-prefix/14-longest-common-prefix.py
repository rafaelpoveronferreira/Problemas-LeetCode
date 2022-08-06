class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = strs[0]
        prefix = ''
        c = 0

        # Find the smallest number in strs list
        for i, _ in enumerate(strs):
            if len(smallest) > len(strs[i]):
                smallest = strs[i]

        # A double for iteration that looks for each character in each string of strs list.
        for char in range(len(smallest)):
            c=0
            for i, _ in enumerate(strs):
                if smallest[char] == strs[i][char]:
                    c += 1
            if c == len(strs):
                prefix += smallest[char]
                c = 0
            else:
                break

        return prefix
