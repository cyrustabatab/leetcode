


def merge_sorted_arrays(a1,a2):


    head = None


    current_1 = a1
    current_2 = a2


    while current_1 or current_2:
        if current_1 and (not current_2 or  current_1.val <= current_2.val):
            result = current_1.val
            current_1 = current_1.next
        else:
            result = current_2.val
            current_2 = current_2.next
        
        new_node = ListNode(result)
        if not head:
            head = result
        else:
            previous.next  = new_node

        previous = new_node


    return head

         
    return result
