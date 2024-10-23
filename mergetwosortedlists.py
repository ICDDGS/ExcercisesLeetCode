from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
                res = ListNode()
                aux = res
                while (list1 or list2):
                    if list1 is None:
                        aux.next = list2
                        aux = aux.next
                        list2 = list2.next
                        #.next = None
                    elif not list2:
                        aux.next = list1
                        aux = aux.next
                        list1 = list1.next
                        #aux.next = None
                    else:
                        if list1.val <= list2.val:
                            aux.next = list1
                            list1 = list1.next
                        else:
                            aux.next = list2
                            list2 = list2.next
                        aux = aux.next
                        aux.next = None

                return res.next