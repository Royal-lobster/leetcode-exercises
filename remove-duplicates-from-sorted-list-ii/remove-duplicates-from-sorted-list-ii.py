class Solution(object):
    def deleteDuplicates(self, head):
        if head == None:
            return head
        p, l, r, d = None, head, head.next, False
        while(r != None):
            if l.val == r.val:
                l.next = r.next
                d, r = True, r.next
            else:
                if d:
                    if p == None : 
                        head = l.next
                    else: 
                        p.next = l.next
                    d = False
                else:
                    p = l
                l, r = l.next, r.next
        if d:
            if p == None :
                head = l.next
            else: 
                p.next = l.next
        return head

                