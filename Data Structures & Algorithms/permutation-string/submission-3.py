from collections import Counter 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        count1=Counter(s1)
        w=Counter(s2[:len(s1)])

        if w ==count1:
            return True

        for r in range(len(s1), len(s2)):
            l=r-len(s1)
            w[s2[r]]+=1
            w[s2[l]]-=1
            if w[s2[l]]==0:
                del w[s2[l]]
                
            if w==count1:
                return True
        return False