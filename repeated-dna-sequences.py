class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]: 
        all_sub = [] 
        for i in range(0, (len(s)-8+1)):
            sub = s[i:i+10]
            all_sub.append(sub)
        unique_sub = set(all_sub)
        answer = [] 
        for sub in unique_sub:
            if s.count(sub) > 1: 
                answer.append(sub)
        return answer


class Solution: #faster than 95%
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        answer = set()
        all_sub = set()
        for i in range(len(s)-10+1):
            sub = s[i:i+10] #a substring
            if sub in all_sub: #if already found --add to answer
                answer.add(sub) #method for sets, not lists
            else:
                all_sub.add(sub) #add to found
        return list(answer)