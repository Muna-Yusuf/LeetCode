# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        tmp = ListNode()  # Temporary node to build the new list
        curr = tmp  # Pointer to the last node in the merged list

        # Merge the two lists
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next  # Move the current pointer forward

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return tmp.next