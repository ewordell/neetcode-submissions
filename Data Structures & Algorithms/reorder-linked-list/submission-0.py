# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        original_head = head
        node_list = []
        visited = set()
        while head:
            node_list.append(head)
            head = head.next

        length = len(node_list)
        head = original_head
        vals = [v.val for v in node_list]
        print(vals)


        for i in range(length//2):
            to_add = node_list[-(i+1)]
            node_list[i].next = to_add
            to_add.next = node_list[i+1] if (i+1)!=((length//2)) else None
            print(f"to_add.val={to_add.val}")
        if length%2 == 1 and length>2:
            to_add.next=node_list[length//2]
            node_list[length//2].next = None

        return None




            

        # for i in range(length // 2):
        #     # print(head.val)
        #     # print(head.next.val)
        #     temp_next = head.next
        #     if i != ((length // 2) - 1):
        #         head.next = node_list[-(i+1)]   
        #     # print(head.next.val)
        #     if not temp_next in visited:
        #         head.next.next = temp_next
        #     head = temp_next
        # head = original_head

        return original_head
        # print(type(original_head))
        # return original_head
            

        