# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return None

        init = ListNode(val=head.val, next=None)

        n = head.next
        while n != None:
            init = ListNode(val=n.val, next=init)
            n = n.next
        
        return init
