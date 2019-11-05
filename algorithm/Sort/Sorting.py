def insertion_sort(A):
    for idx in range(1,len(A)):#1...len(A)-1
        key = A[idx]
        cmp_idx = idx-1
        while cmp_idx>=0 and A[cmp_idx]>key:
            A[cmp_idx+1]=A[cmp_idx]
            cmp_idx -= 1
        A[cmp_idx+1] = key

def partition(A, start, end):
    pivot_idx = end-1
    mid_idx = start
    for cmp_idx in range(start, pivot_idx):
        if A[cmp_idx] <= A[pivot_idx]:
            A[mid_idx],A[cmp_idx] = A[cmp_idx],A[mid_idx]
            mid_idx += 1
    A[mid_idx],A[pivot_idx] = A[pivot_idx],A[mid_idx]
    return mid_idx

def quick_sort(A, start=0, end=None):
    if end is None:
        end = len(A)
    if start < end:
        mid = partition(A, start, end)
        quick_sort(A, start, mid)#start...mid-1
        quick_sort(A, mid+1, end)#mid+1...end-1

def merge(left, right):
    result = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    #Copy remaining elements...
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

def merge_sort(A):
    if len(A)<=1:
        return A
    mid = len(A) // 2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    return merge(left, right)

def max_heapify(A, root_idx, heap_size):
    left_idx = 2*root_idx + 1
    right_idx = 2*root_idx + 2
    max_idx = root_idx
    if left_idx < heap_size and A[left_idx]>A[max_idx]:
        max_idx = left_idx
    if right_idx < heap_size and A[right_idx]>A[max_idx]:
        max_idx = right_idx
    if max_idx != root_idx:
        A[root_idx], A[max_idx] = A[max_idx],A[root_idx]
        max_heapify(A, max_idx, heap_size)

def build_max_heap(A):
    for idx in range(len(A)//2,-1,-1):#len(A)//2...0
        max_heapify(A, idx, len(A))

def my_heap_sort(A):
    build_max_heap(A)
    for heap_size in range(len(A)-1, 0, -1):#len(A)-1...1
        A[0],A[heap_size] = A[heap_size],A[0]
        max_heapify(A, 0, heap_size)
#import heapq
#def heapsort(iterable):
#    h = []
#    for value in iterable:
#        heapq.heappush(h, value)
#    return [heapq.heappop(h) for i in range(len(h))]

def counting_sort(str):
    counter = [ 0 for i in range(26) ]
    result = [char for char in str]
    
    for char in str:
        char_index = ord(char)-ord('a')
        counter[char_index] += 1
    
    for i in range(1, len(counter)):
        counter[i] += counter[i-1]
    
    for char in reversed(str):
        char_index = ord(char)-ord('a')
        result[counter[char_index]-1] = char
        counter[char_index] -= 1
    
    return ''.join(result)

if __name__ == "__main__": 
    A = [ 1, 4, 2, 3, 9, 8, 7, 16, 14, 10 ]

    #insertion_sort(A)
    #print("After insertion_sort: {}".format(A))

    #print("merge_sort: {}".format(merge_sort(A)))
    #print("After merge_sort: {}".format(A))

    my_heap_sort(A)
    print("After my_heap_sort: {}".format(A))

    #quick_sort(A)
    #print("After quick_sort: {}".format(A))
    
    #print("counting_sort: {}".format(counting_sort("traceback")))
