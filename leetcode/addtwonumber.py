# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = "", ""
        while l1:
            n1= n1 + str(l1.val)
            l1 = l1.next
        while l2:
            n2 = n2 + str(l2.val)
            l2 = l2.next
        if n1 == "": n1 = "0"
        if n2 == "": n2 = "0"
        sum = int(n1) + int(n2)
        sumList = ListNode()
        for i in reversed(str(sum)):
            sumList.next = ListNode(i)
            sumList = sumList.next
        return sumList

l1=[2,4,3]
l2=[5,6,4]
print(addTwoNumbers(l1,l2))