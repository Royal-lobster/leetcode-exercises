class Solution(object):
    def middleNode(self, head):
        # find length of the linked list
        current_node, list_length = head, 0
        while current_node != None:
            list_length += 1
            current_node = current_node.next
        
        # find index of middle element
        middle_index = list_length//2
        
        print([list_length, middle_index])
        
        # iterate through list till middle element and return it
        current_node = head
        for x in range(middle_index):
            list_length += 1
            current_node = current_node.next
        return current_node