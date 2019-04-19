class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        #the hypothesis is possible only 
        #if the sum of all numbers in an array can be equally divided without the rest
        if sum_nums % 2 != 0:  #just for understanding, this is covered by the last return statement
            return False
        else:
            possible_sums = {0} #empty dict with possible sums
            for n in nums: #for each number 
                #print(n)
                #print(possible_sums)
                possible_sums.update({(v + n) for v in possible_sums}) #adds sums and itself becaue sum with 0 is always itself 
                # it updates dictionary 
                # with n element and all possible sums of n and elements in the dictionary
                # and stores only unique elements
                #print(possible_sums)
            return (sum_nums / 2)  in possible_sums  
            # если полусумма есть в возможных сабсетах, значит другую полусумму можно будет собрать из                      оставшихся чисел. (Так как сумма делится на два без остатка). Даже если полусумма не делится на                два без остаткаа, такую полусумму не может быть в возможных суммах, что априори выдает false. 
            # if halfsum is in possible_sums, it means that our array can be divided by 2 equal subsets 
            # example 1 [3,2,6,1]
            # its sum is 12, halfsum is 6
            # halfsum is in possible_sums (3+2+1), so the array can be divided in 2 subsets
            # example 2 
            # [12] possible_sums = {12}
            # 12/2 = 6 is not there, so false 
            # example 3 
            # [3,2,6,1,6]
            # halfsum = 9 
            # 9 is in possible sums (6+1+2) 
            # then the rest can be made from the rest numbers
            
            

        