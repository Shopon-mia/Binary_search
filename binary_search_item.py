def binary_search(list, search_item):
    low_index = 0
    high_index = len(list - 1)

    while low_index <= high_index:

        mid = (low_index + high_index) // 2
        
        if list[mid] == search_item:
            print("Value found at index : ", mid)
            return
        if list[mid] < search_item:
            low_index = mid + 1
        if list[mid] > search_item:
            high_index = mid - 1
    print("OOPS!!... value is not found")

list = [10, 20, 30, 40, 50, 60, 70, 80]
binary_search(list, search_item=100)