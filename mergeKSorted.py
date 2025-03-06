"""
heap (priority queue) approach
TC - O(nk log k) ==> n is the avg length of lists, k is number of lists
log k is comparison time for heap operations
SC - O(k) to perform heap operations
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # create a custom (lambda) lessThan comparator to compare two nodes
        lessThan = lambda x, y: x.val < y.val
        ListNode.__lt__ = lessThan

        # create a dummy node for new merged LL
        dummy = ListNode(-1)

        curr = dummy

        heap = []

        # traverse through list to get each sublist
        for i in range(len(lists)):
            # sublist
            currHead = lists[i]
            print(currHead)
            if currHead is not None:
                heapq.heappush(heap, currHead)

        while heap:
            # pop lowest element
            minnode = heapq.heappop(heap)

            # point curr's next to minnode , i.e. add popped node to new LL
            curr.next = minnode

            # from the original LL, check if there's an element present after the current popped element
            # i.e. minnode is the current popped element
            # if next element is present, push it to the heap
            if minnode.next is not None:
                heapq.heappush(heap, minnode.next)

            # point curr to the next element
            curr = minnode

        return dummy.next