# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        done = False
        node = self.nextNode(list1, list2)

        return node
    
    def nextNode(self, p1, p2):
        if p1 == None and p2 != None:
            return ListNode(val=p2.val, next=self.nextNode(p1, p2.next))
        elif p2 == None and p1 != None:
            return ListNode(val=p1.val, next=self.nextNode(p1.next, p2))
        elif p1 == None and p2 == None:
            return None
        if p1.val <= p2.val:
            return ListNode(val=p1.val, next=self.nextNode(p1.next, p2))
        else:
            return ListNode(val=p2.val, next=self.nextNode(p1, p2.next))