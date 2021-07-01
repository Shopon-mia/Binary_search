def charecter_binary(Letters, target):
    start = 0
    end = len(Letters) - 1
    while start <= end:
        middle = (start + end)// 2
        midpoint = Letters[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return middle

Letters = ["A", "B", "C", "D", "E", "F"]
found = charecter_binary(Letters, "E")
print("Search letter found at ",found," index")
