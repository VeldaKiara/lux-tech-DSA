'''
use 2 pointers
current pointer to 1st node then prev to null
reverse 1st node then shift pointers to the next nodes
at the end the prev pointer should point to the head
'''
class Solution:
    def reverseList(self, head):
        #create pointers
        prev, curr = None, head
        #shift pointers
        while curr:
            #temp var for nexts, to be able to update curr.next
            nexts = curr.next
            curr.next = prev
            prev = curr
            curr = nexts
        return prev

        