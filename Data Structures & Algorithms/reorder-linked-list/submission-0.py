# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # slow, fast = head, head

        # while fast and fast.next:
        #     slow = head.next
        #     fast = fast.next.next

        # pre, cur = None, slow
        # while cur:
        #     nextNode = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = nextNode
        
        # first, second = head, pre
        # while second.next:
        #     temp1, temp2 = first.next, second.next
        #     first.next = second 
        #     second.next = temp1
        #     first = temp1
        #     second = temp2
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # step 2 : reverse second half
        prev, curr = None, slow
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        # step 3: merge the second half and first
        first, second = head, prev
        while second.next:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
