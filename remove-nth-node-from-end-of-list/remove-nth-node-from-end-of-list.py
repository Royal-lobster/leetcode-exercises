class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n): 
            fast = fast.next
        if fast == None: 
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
