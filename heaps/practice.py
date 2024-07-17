from heaps.heap import Heap
import heapq


class Practice:

  def insert_in_heap(self):
    # arr = [-1, 100, 50, 60, 40, 45]
    # arr = []
    # heap = Heap(arr)

    # print(heap.arr)
    # heap.insert(50)
    # heap.insert(30)
    # heap.insert(70)
    # heap.insert(40)
    # heap.insert(80)
    # heap.insert(100)
    # print(heap.arr)

    # heap.deletion()
    # print(heap.arr)

    # arr = [12, 15, 13, 11, 14]
    # arr = [12, 56, 43, 6, 78, 87, 5, 44, 3, 23, 32]
    # n = len(arr)
    # h = Heap()
    # result = h.build_heap(arr, n)
    # print(result)

    arr = [12, 56, 43, 6, 78, 87, 5, 44, 3, 23, 32]
    h = Heap()
    result = h.heap_sort(arr)

    print(result)

  def priority_queue(self):
    """
    """
    # li = [10, 100, 200, 300, 400, 500, 150, 250, 350, 450]
    # li = []
    # heapq.heappush(li, 1)
    # heapq.heappush(li, 5)
    # heapq.heappush(li, 16)
    # heapq.heappush(li, 11)
    # heapq.heappush(li, 9)
    # heapq.heappush(li, 2)
    # heapq.heappush(li, 7)

    # print(li)
    # print(heapq.heappop(li))
    # print(heapq.heappop(li))

    customers = []
    heapq.heappush(customers, (2, "Harry"))
    heapq.heappush(customers, (3, "Charles"))
    heapq.heappush(customers, (1, "Riya"))
    heapq.heappush(customers, (4, "Stacy"))
    print(customers)
    while customers:
      print(heapq.heappop(customers))
