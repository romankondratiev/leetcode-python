# Easy solution with filter
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        #Array (list) with non-negative integers
        #Array with integers : even, odd 
        even = list(filter(lambda x: x%2 == 0, A)) #sort out even
        odd = list(filter(lambda x: x%2 == 1, A)) #sort out odd
        return even + odd #returning merged list

# Another easy solution (without filter function)
class Solution:
    def sortArrayByParity(self, A: [0]) -> List[int]:
        #Array (list) with non-negative integers
        #Array with integers : even, odd 
        def even(n):
            if n % 2 == 0:
                return n 
        def odd(n):
            if n % 2 == 1:
                return n 
        answer = []
        for i in A:
            if even(i) == i: #if without ==i part, evaluetes 0%2 as false and list with 0 will not                                work as a test case
                answer.append(i)
        for i in A:
            if odd(i) == i:
                answer.append(i)
        return answer

# Recursive / Botton-up / Functional (working only in only in external editors for some reasons)
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if len(A) == 1:
            return A
        if A[0] %2 == 0: #if even  
            return [A[0]] + sortArrayByParity(A[1:]) #return it and rec call with list w/o this el
        else: # else recursive call without this element + this element by the end 
            return sortArrayByParity(A[1:]) + [A[0]]