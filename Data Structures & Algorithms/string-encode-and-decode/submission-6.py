class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for ele in strs:
            le = len(ele)
            s += str(le)
            s += "#"
            s += ele
        return s


    def decode(self, s: str) -> List[str]:

        i = 0
        store = []

        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1
            
            le = int(s[i : j])

            word = s[j+1 : le+j+1]
            store.append(word)

            i = le + j + 1
        
        return store