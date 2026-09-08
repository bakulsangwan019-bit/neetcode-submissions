class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dii = {}

        for i in strs:
            count = [0] * 26

            for j in i:
                word = ord(j) - ord("a")
                count[word] += 1

            a = tuple(count)

            if a not in dii:
                dii.setdefault(a,[])
                
            dii[a].append(i)

        return list(dii.values())
            