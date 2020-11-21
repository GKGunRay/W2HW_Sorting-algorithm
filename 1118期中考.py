# 20201121

def Selction_Sort(numarr):
    # 目的：以選擇排序法由左到右、大到小排列數列。
    # 掃描數列中所有的數值作選擇排序法
    for i in range(len(numarr)-1):
        # 第 i 次的起始位置，下面處理尋找數列中的最大值
        maximum = i
        # 從第 i+1 項開始、未排列的數列中尋找下列if的條件
        for j in range(i+1, len(numarr)):
            # 尋找未排列數列中，比numarr[maximum]還要大的數值
            if numarr[j] > numarr[maximum]:
                # 找到第 j 項比 i 還要大，maximum 存入 j 值
                maximum = j

        # 第二大的numarr[i]與最大的numarr[maximum]互換，此為排列
        numarr[i], numarr[maximum] = numarr[maximum], numarr[i]
        # 輸出此次排列的結果（類JS三元運算式的寫法）
        txt = "原始陣列\t：" if i == 0 else "第"+str(i)+"次排序\t："
        print(txt, numarr)
    return numarr

def insertionSort(numarr):
    # 目的：將給定的數列由左到右、小到大，以插入排序法排列。
    # 將數列中所有的數字都掃描過一次，作插入排序法。
    for i in range(len(numarr)):
        # 已排列的數列（長度）：
        sortedIndex = i-1
        # 當前指向的數列項，也作temp使用：
        current = numarr[i]
        # 當存在已排列的數列 以及 從第 i - 1 項往第 0 項尋找可以插入current的位置
        # （插入的同時也是排列）
        while sortedIndex >= 0 and numarr[sortedIndex] > current:
            # 移動數列
            numarr[sortedIndex+1] = numarr[sortedIndex]
            # 索引值 - 1 來搜尋前一個數列項
            sortedIndex-=1
        # sortedIndex+1是current的插入位置
        numarr[sortedIndex+1] = current
        # 輸出該次插入的結果（類JS三元運算式的寫法）
        txt = "原始陣列\t：" if i == 0 else "第"+str(i)+"次排序\t："
        print(txt, numarr)
    return numarr

if __name__ == '__main__':
    import random
    a = list(range(8))
    random.shuffle(a)
    b = a
    print("Selection sort, from left to right, from large to small:")
    a = Selction_Sort(a)
    print()
    print("Insertion sort, from left to right, from small to large:")
    b = insertionSort(b)
