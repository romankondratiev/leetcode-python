class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        #input : ["cba","daf","ghi"]
        A = zip(*A) #basically UNZIP the list by making a list with tuples; each with elements of the same index
        # print(list(A)) >>> [('c', 'd', 'g'), ('b', 'a', 'h'), ('a', 'f', 'i')]
        output = 0
        for col in A: #for tuple in A
            if list(col) != sorted(col):
                output += 1 #if not sorted - needs deletion
        return output


#------About zip() built-in method -----
# >>> x = [1, 2, 3]
# >>> y = [4, 5, 6]
# >>> zipped = zip(x, y)
# >>> list(zipped)
# [(1, 4), (2, 5), (3, 6)]
# unzip with *
 