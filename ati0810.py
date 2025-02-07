class ListNode:  
    def __init__(self, val=0, next=None):  
        self.val = val  
        self.next = next  

def deleteDuplicates(head: ListNode) -> ListNode:  
    current = head  

    while current and current.next:  
        if current.val == current.next.val:  
             
            current.next = current.next.next  
        else:  
            current = current.next   
            
    return head  


def create_linked_list(lst):  
    if not lst:  
        return None  
    
    head = ListNode(lst[0])  
    current = head  
    for value in lst[1:]:  
        current.next = ListNode(value)  
        current = current.next  
    return head  


def linked_list_to_list(head):  
    lst = []  
    current = head  
    while current:  
        lst.append(current.val)  
        current = current.next  
    return lst  


input_list = [1, 1, 2, 2, 3, 3]  
head = create_linked_list(input_list)  
new_head = deleteDuplicates(head)  
output_list = linked_list_to_list(new_head)  

print(output_list) 