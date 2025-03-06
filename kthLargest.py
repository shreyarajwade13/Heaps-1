# TC - O(n log k) - since size if heap is k and we are performing operations n times
# SC - O(k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums is None or len(nums) == 0: return -1

        # heapq.heapify(nums)

        # print(nums)

        # n_largest = heapq.nlargest(2, nums)
        # print(n_largest) --> order is not maintained in heaps so no way to know if 0th index or 1st index
        # is the required output

        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                # since min heap, we lose (pop) the smallest element
                heapq.heappop(heap)
        return heap[0]


        # to get kth smallest element --
        # for num in nums:
        #     heapq.heappush(heap, num)
        #     for i in range(k-1):
        #         if len(heap) > n - k:
        #             result = heapq.heappop(heap)
        # return result
        #