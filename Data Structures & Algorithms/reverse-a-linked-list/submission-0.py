# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        if cur is None:
            return None
        while cur:
            new_node = ListNode(val=cur.val, next = prev)
            # res.append(new_node)
            prev = new_node
            cur = cur.next
            print(new_node.val)

        return new_node

        
        