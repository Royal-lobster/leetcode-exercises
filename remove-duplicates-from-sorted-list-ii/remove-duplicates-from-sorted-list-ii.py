class Solution(object):
    def deleteDuplicates(self, head):
        
        if head == None:
            return head
        
        p, l, r, d = None, head, head.next, False
        
        # TREVERSE THE LIST
        while(r != None):
            print(p.val if p else p, [l.val, r.val])
            # IF WE FOUND THE DUBLICATE NUMBER, MARK IT AND DELETE
            if l.val == r.val:
                l.next = r.next # delete r from list
                print("deleted ", r.val)
                d, r = True, r.next # mark duplicate found and move r
            
            # NO DUBLICATE FOUND IN THIS ITERATION
            else:
                # IF DUBLICATE FOUND IN PREVIOUS ITERATIONS, DELETE THAT HERE
                if d:
                    if p == None : 
                        head = l.next # delete l from list
                    else: 
                        p.next = l.next # delete l from list
                    d = False
                    print("deleted source", l.val)
                else:
                    p = l
                l, r = l.next, r.next
        if d:
            if p == None :
                head = l.next # delete l from list
            else: 
                p.next = l.next # delete l from list
        return head

                