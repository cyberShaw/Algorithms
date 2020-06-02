# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = head
        stack = []
        l = 0
        while temp:
            l += 1
            temp = temp.next
        temp = head
        for i in range(0, l//2):
            stack.append(temp.val)
            temp = temp.next
        if l % 2 != 0:
            temp = temp.next
        for i in range(0, l//2):
            if temp.val == stack.pop():
                continue
            return False
        return True