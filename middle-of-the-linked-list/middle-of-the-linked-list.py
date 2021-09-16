class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
            