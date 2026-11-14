class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    
        a = False
        if len(s1) <= len(s2):
            if len(s1) <= len(s2):
                freq = [0] * 26
                w_f = [0] * 26


                for i in range(len(s1)):
                    freq[ord(s1[i]) - ord('a')] += 1
                    w_f[ord(s2[i]) - ord('a')] += 1

                if freq == w_f:
                    a = True

                current = 0


                if not a:
                    for i in range(len(s1), len(s2)):
                        w_f[ord(s2[i]) - ord('a')] += 1
                        w_f[ord(s2[current]) - ord('a')] -= 1
                        current += 1

                        if w_f == freq:
                            a = True
                            break
            
        return a 