from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        base = ord("a")

        for word in strs:
            count = [0] * 26

            for char in word:
                index = ord(char) - base
                count[index] += 1

            groups[tuple(count)].append(word)

        return list(groups.values())