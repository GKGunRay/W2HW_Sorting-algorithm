#20200930
"""
def Insertion_Sort(datas):
    for i in range(1, len(datas)):  # 
        for j in range(i):
            current = datas[i]
            if current < datas[j]:
                for k in range(i,j):
                  print(datas)
    return datas
"""

def insertionSort(arr):
    big_o = [1, 0, 0] #big_o，這行不算入，分別為0、1、2次方
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex-=1
            big_o[2] += 2 #不算入執行次數
        arr[preIndex+1] = current
        print(arr)
        big_o[1] += 3 #不算入執行次數
    return [arr, big_o]
    #執行次數：(arr[preIndex] > current個)(n+1)+3n+1
    #時間複雜度：n~n^2

if __name__ == '__main__':
    import random
    a = list(range(10))
    random.shuffle(a)
    b = a.copy()

    arr = insertionSort(a)
    #a2 = Insertion_Sort(a)
    #print(arr)
    print('---'*10)
    print("實際執行次數：\t\t\t" + str(arr[1][0]+arr[1][1]+arr[1][2]))
    print("i goes from 1 to n, sigma i:\t" + str(arr[1][2]))
    print("n:\t\t\t\t" + str(arr[1][1]))
    print("個位：\t\t\t\t" + str(arr[1][0]))
    print('---'*10)
    print("Big-O: n*(i goes from 1 to n, sigma i)")
    #print(a2)

