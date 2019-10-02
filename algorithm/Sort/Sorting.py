def insertion_sort(A):
    for key_index in range(1,len(A)):#1...len(A)-1
        key_value = A[key_index]
        compare_index = key_index-1
        while compare_index>=0 and A[compare_index]>key_value:
            A[compare_index+1]=A[compare_index]
            compare_index -= 1
        A[compare_index+1] = key_value

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index<len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:len(left)])
    result.extend(right[right_index:len(right)])
    return result

def merge_sort(A):
    if len(A)<=1:
        return A
    mid = len(A) // 2
    left = merge_sort(A[0:mid])
    right = merge_sort(A[mid:len(A)])
    return merge(left, right)

def max_heapify(A, root_index, heap_size):
    left_index = 2*root_index + 1
    right_index = 2*root_index + 2
    max_index = root_index
    if left_index < heap_size and A[left_index]>A[max_index]:
        max_index = left_index
    if right_index < heap_size and A[right_index]>A[max_index]:
        max_index = right_index
    if max_index != root_index:
        A[root_index], A[max_index] = A[max_index],A[root_index]
        max_heapify(A, max_index, heap_size)

def build_max_heap(A):
    for index in range(len(A)//2,-1,-1):#len(A)//2...0
        max_heapify(A, index, len(A))

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

def partition(A, start, end):
    pivot_index = end-1
    mid_index = start
    for large_index in range(start, pivot_index):
        if A[large_index] <= A[pivot_index]:
            A[mid_index],A[large_index] = A[large_index],A[mid_index]
            mid_index += 1
    A[mid_index],A[pivot_index] = A[pivot_index],A[mid_index]
    return mid_index

def quick_sort(A, start=0, end=None):
    if end is None:
        end = len(A)
    if start < end:
        mid = partition(A, start, end)
        quick_sort(A, start, mid)#start...mid-1
        quick_sort(A, mid+1, end)#mid+1...end-1

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

    #my_heap_sort(A)
    #print("After my_heap_sort: {}".format(A))

    quick_sort(A)
    print("After quick_sort: {}".format(A))
    
    print("counting_sort: {}".format(counting_sort("traceback")))
