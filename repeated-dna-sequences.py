class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #if len(s) == 10: 
            #return [s]
        #else: 
        all_sub = [] 
        for i in range(0, (len(s)-9)):
            sub = s[i:i+10]
            all_sub.append(sub)
        unique_sub = set(all_sub)
        answer = [] 
        for sub in unique_sub:
            if s.count(sub) > 1: 
                answer.append(sub)
        return answer