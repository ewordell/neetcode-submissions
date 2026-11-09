# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_pointer = head
        slow_pointer = head
        while fast_pointer:
            for _ in range(2):
                fast_pointer=fast_pointer.next
                if fast_pointer == slow_pointer:
                    return True
                if not fast_pointer:
                    return False
            slow_pointer = slow_pointer.next
        return False
        