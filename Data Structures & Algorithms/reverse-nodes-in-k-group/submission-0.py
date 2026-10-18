# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        grouppre = dummy 

        while True:
            kth = self.getKth(grouppre, k)
            if not kth:
                break
            groupNext= kth.next

            pre, curr = kth.next, grouppre.next
            while curr != groupNext:
                temp = curr.next
                curr.next = pre
                pre = curr
                curr = temp
            temp = grouppre.next
            grouppre.next = kth
            grouppre = temp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0: 
            curr = curr.next
            k -= 1
        return curr