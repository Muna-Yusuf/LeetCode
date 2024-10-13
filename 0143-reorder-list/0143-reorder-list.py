# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        per = None
        cur = slow
        while cur:
            next_tmp = cur.next
            cur.next = per
            per = cur
            cur = next_tmp
        
        f1 = head
        s2 = per
        while s2.next:
            tmp1 = f1.next
            tmp2 = s2.next
            f1.next = s2
            s2.next = tmp1
            
            # Move the pointers forward
            f1, s2 = tmp1, tmp2