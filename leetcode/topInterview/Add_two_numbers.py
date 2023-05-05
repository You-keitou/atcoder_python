# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        ans: Optional[ListNode] = ListNode()
        cur_node = ans

        while(l1 or l2):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            cur_node.val += (val1 + val2) % 10
            kuriage = 0
            if cur_node.val >= 10:
                kuriage = 1
                cur_node.val = cur_node.val % 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur_node.next = ListNode((val1 + val2) // 10 + kuriage) if l1 or l2 or kuriage or (val1 + val2)//10  else None
            cur_node = cur_node.next

        return ans

a = ListNode(5)
b = ListNode(5)

sol = Solution()
sol.addTwoNumbers(a,b)
