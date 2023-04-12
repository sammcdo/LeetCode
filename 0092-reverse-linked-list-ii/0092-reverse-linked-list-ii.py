# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        l = []
        while head:
            if left <= i and i <= right:
                l.insert(left-1, head.val)
            else:
                l.append(head.val)
            head = head.next
            i += 1
        
        p = None
        for i in range(len(l)-1, -1, -1):
            p = ListNode(val=l[i], next=p)
        
        return p
        