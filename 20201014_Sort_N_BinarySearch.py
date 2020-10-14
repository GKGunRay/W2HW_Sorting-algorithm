def binarySearch(data, left, right, target):
    while True:
        if right >= left:
            mid = left + (right - left) // 2
            if data[mid] == target:
                return mid
            elif data[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return -1

def binarySearchOriginal(data, left, right, target):
    if right >= left:
        mid = left + (right - left) // 2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            return binarySearch(data, left, mid - 1, target)
        else:
            return binarySearch(data, mid + 1, right, target)
    else:
        return -1

def InsertionSort(arr):
    print("Sorting...")
    i = 1
    while i < len(arr):
        j = i - 1
        temp = arr[i]
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j-=1
        arr[j + 1] = temp
        print(arr)
        i += 1
    return arr

data = []
print("Please input number(s) for data for sorting:")
while True:
    ip = input()
    if ip != '':
        data.append(int(ip))
    else:
        break

data = InsertionSort(data)
print("---"*10)
    
targets = []
print("Please input number(s) for searching in your data:")
while True:
    sch = input()
    if sch != '':
        targets.append(int(sch))
    else:
        break

print("Result:\n"+"---"*10)
print("binarySearch(Loop):")
for i in range(len(targets)):
    result = binarySearch(data, 0, len(data)-1, targets[i])
    if result != -1:
        print("元素在索引 %d" % result)
    else:
        print("陣列中找不到該元素")

print("\nbinarySearch(Recursive):")
for i in range(len(targets)):
    result = binarySearchOriginal(data, 0, len(data)-1, targets[i])
    if result != -1:
        print("元素在索引 %d" % result)
    else:
        print("陣列中找不到該元素")


