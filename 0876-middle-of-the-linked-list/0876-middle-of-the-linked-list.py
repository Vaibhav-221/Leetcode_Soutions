# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        if not head or not head.next:
            return head
        after = head
        before = head
        while after and after.next:
            after = after.next.next
            before = before.next
        return before

        
       

        