# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        current = remove = prev = head
        count = 0 
        while current != None:
            if n != -1: n-=1
            if n == -1:
                prev = remove
                remove = remove.next
            current = current.next
        if prev == remove == head: head = head.next
        prev.next = remove.next
        return head
