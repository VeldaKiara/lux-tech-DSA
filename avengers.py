"""
create a func
dfs, recursive, create helper func with boundaries that is left and right
inside helper func:
check if node is empty, rem empty node is still binary tree
check if the tree obeys root > left,  root < right, if not satisified, not binary return False
recurse, call the func again to chech the left subtree, right subtree, rem "nlr" 
check the left subtree, values on the left have to be less than the node val, set the parent to the right boundary, 
check the right subtree, values on the right are > than node val, right boundary set to right, 
then combine checks set to true, -> true vice versa
return func with root and -inf set to left values can be anything

Time Complexity: O(n)
Space Complexity: O(nm), n-parent nodes, m-child nodes
"""

class Solution:
    def isValidBST(self, root):
        
        def checkValid (node, left, right):
            
            if not node:
                return True
            
            if not (node.val > left and node.val < right):
                return False
            
            return (checkValid (node.left, left, node.val) and 
                    checkValid(node.right, node.val, right)) 
        
        return checkValid(root, float("-inf"), float("inf"))