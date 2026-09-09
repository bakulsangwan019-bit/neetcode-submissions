class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dii ={}
        outp = []

        for val in nums:
            if val not in dii:
                dii[val] = 1
            else:
                dii[val] += 1
            
        sor = sorted(dii.items() ,key = lambda x : x[1],reverse = True)
        
        for a, b in sor:

            if len(outp) < k:
                outp.append(a)

        return outp