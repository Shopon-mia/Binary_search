def binary_search(number_list, search_item):
    low_index = 0
    high_index = len(number_list)-1

    while low_index <= high_index:

        mid = (low_index + high_index) // 2
        
        if number_list[mid] == search_item:
            print("Value found at index : ", mid)
            return
        if number_list[mid] < search_item:
            low_index = mid + 1
        if number_list[mid] > search_item:
            high_index = mid - 1
    print("OOPS!!... value is not found")

number_list = [10, 20, 30, 40, 50, 60, 70, 80]
binary_search(number_list, search_item=100) 