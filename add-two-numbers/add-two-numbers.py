# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a1 = []
        a2 = []
        ptr1 = l1
        ptr2 = l2
        while(ptr1 != None):
            a1.append(str(ptr1.val))
            ptr1 = ptr1.next
        while(ptr2 != None):
            a2.append(str(ptr2.val))
            ptr2 = ptr2.next
        a1 = a1[::-1]
        a2 = a2[::-1]
        num1 = "".join(a1)
        num2 = "".join(a2)
        result = str(int(num1)+int(num2))[::-1]
        l3 = ListNode()
        ptr3 = l3
        for x in range(len(result)-1):
            ptr3.val = int(result[x])
            ptr3.next = ListNode()
            ptr3 = ptr3.next
        ptr3.val = int(result[-1])
        return l3