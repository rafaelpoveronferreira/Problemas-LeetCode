# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resultlistnode = None
        resultlist = []
        result = int()
        nxt = 0
        
        # Each digit of the integer numbers correspond to a iteration of the While Loop
        while True:
            result = l1.val + l2.val + nxt

            # If the number have more than one digit, pass the excess to the next iteration
            if result >= 10:
                nxt = 1
                result -= 10
            else:
                nxt = 0
            
            # Add the value of the ListNode to a temporary list.
            resultlist.append(result)

            #if both ListNodes are finished, procced to return the sum ListNode.
            if l1.next == None and l2.next == None:
                # Checks if there is a final digit to add to the list
                if nxt == 1:
                    resultlist.append(nxt)
                
                # Transform the result list into a ListNode
                for num in resultlist[::-1]:
                    resultlistnode = ListNode(num, resultlistnode)
                
                # Return the sum ListNode
                return resultlistnode

            # Refreshes the l1 to the next digit
            if l1.next is not None:
                l1 = l1.next
            else:
                l1 = ListNode()
            if l2.next is not None:
                l2 = l2.next
            else:
                l2 = ListNode()
