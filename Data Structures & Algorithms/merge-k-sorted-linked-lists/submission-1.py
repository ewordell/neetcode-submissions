# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        min_set = set([head.val for head in lists])
        d = defaultdict(list)

        for head in lists:
            val = head.val
            d[val].append(head)

        orig_head = d[min(min_set)][0]
        while min_set: 
            next_val = min(min_set)
            min_set.remove(next_val)

            length = len(d[next_val])
            l = d[next_val]

            del d[next_val]
            for i in range(length):


                head = l[i]
                if head.next:
                    min_set.add(head.next.val)
                if head.next and head.next not in d[head.next.val]:
                    d[head.next.val].append(head.next)

                
                if i != (length-1):
                    head.next = l[i+1]
                elif min_set and d[min(min_set)]:
                    head.next = d[min(min_set)][0]
                else:
                    head.next = None
            

        return orig_head
                #need to know if 
        





        