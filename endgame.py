'''
dynamic programming
have an initial array with ones, base cases 0 nodes = 1 tree, 1 nodes = 1 tree

create a func,
all nodes from 1 to n will be considered as root node, but arr start from 0, need a base case
since 0 nodes -> 1 tree, 1 node -> 1, initialize all nodes to 1's, number trees
start at 2
loop through the range from 2, n+1
total var to store uniques bst
consider each val as root
get subtree valuus on the right and left, left -> root - 1, right -> total nodes - root

update total  from the cache numberTrees, 
return total
time -> O(n2)-> iterate through each node in order
space -> O(n) storing the total unique bst

'''
class Solution:
    def numTrees(self, n):
        
        numberTrees = [1] * (n + 1)
        for nodes in range(2, n + 1):
            total= 0
            #consider each value as a root
            for root in range(1, nodes + 1):
                #getting values of subtrees on the right and left
                left = root - 1
                right = nodes - root
                #add to total for each iteration
                total += numberTrees[left] * numberTrees[right] 
            numberTrees[nodes] = total
            #return the single node
        return numberTrees[n]
                
                
        
        
        
        