def binarySearch(array, target):
    left = 0
    right = len(array)
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        if target < array[mid]:
            right = mid
        else:
            left = mid + 1
    return None


def binarySearchFirstOccurrence(array, target):
    left = 0
    right = len(array)
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] == target and \
                (mid == 0 or array[mid - 1] != target):
            return mid
        if target < array[mid]:
            left = mid + 1
        else:
            right = mid
    return None


def binarySearchFirstLarge(array, k):
    left = 0
    right = len(array)
    firstLarge = None
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] == k and mid + 1 != len(array) and array[mid] != k:
            return mid + 1
        if array[mid] > k:
            right = mid
            firstLarge = mid
        else:
            left = mid + 1
    return firstLarge


def binarySearchLastSmall(array, k):
    left = 0
    right = len(array)
    last_small = None
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] == k and mid != 0 and array[mid - 1] != k:
            return mid - 1
        if array[mid] < k:
            last_small = mid
            left = mid + 1
        else:
            right = mid
    return last_small


if __name__ == "__main__":
    array = [1, 1, 1, 1, 2, 2, 3, 4, 5, 5, 7, 7, 9, 11]
    print('binarySearch')
    print(binarySearch(array, 1))
    print(binarySearch(array, 2))
    print(binarySearch(array, 9))
    print(binarySearch(array, 10))
    print('binarySearchFirstOccurrence')
    print(binarySearchFirstOccurrence(array, 1))
    print(binarySearchFirstOccurrence(array, 2))
    print(binarySearchFirstOccurrence(array, 10))
    print('binarySearchFirstLarge')
    print(binarySearchFirstLarge(array, 1))
    print(binarySearchFirstLarge(array, 7))
    print(binarySearchFirstLarge(array, 10))
    print(binarySearchFirstLarge(array, 0))
    print(binarySearchFirstLarge(array, 13))
    print('binarySearchLastSmall')
    print(binarySearchLastSmall(array, 2))
    print(binarySearchLastSmall(array, 1))
    print(binarySearchLastSmall(array, 11))
    print(binarySearchLastSmall(array, 4))
    print(binarySearchLastSmall(array, 6))
