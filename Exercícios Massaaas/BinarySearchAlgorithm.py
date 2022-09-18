class BinarySearch():
    def __init__(self, array):
        self.array = array
        self.array.sort()

    def search(self, value):
        low = 0
        high = len(self.array) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.array[mid] == value:
                return mid
            elif self.array[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
        return -1


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    binary_search = BinarySearch(array)
    print(binary_search.search(5))
