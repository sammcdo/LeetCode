/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        return nextNode(list1, list2);
    }

    public ListNode nextNode(ListNode p1, ListNode p2) {
        if (p1 == null && p2 != null) {
            return new ListNode(p2.val, nextNode(p1, p2.next));
        }
        if (p1 != null && p2 == null) {
            return new ListNode(p1.val, nextNode(p1.next, p2));
        }
        if (p1 == null && p2 == null) {
            return null;
        }
        if (p1.val <= p2.val) {
            return new ListNode(p1.val, nextNode(p1.next, p2));
        } else {
            return new ListNode(p2.val, nextNode(p1, p2.next));
        }
    }
}