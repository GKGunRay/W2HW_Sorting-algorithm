#20200930
def Selction_Sort(datas):
    big_o = [1, 0, 0] #big_o，這行不算入，分別為0、1、2次方
    for i in range(len(datas)-1):
        min = i # 第一次選從第一個數開始,第二次從第二個數開始
        for j in range(i+1, len(datas)):    # 用記錄的max數與其他的比較
            if datas[j] < datas[min]:
                min = j
                big_o[2] += 1 #不算入執行次數
        datas[i], datas[min] = datas[min], datas[i]
        big_o[1] += 1 #不算入執行次數（還是算3？）
        print(datas)
    return [datas, big_o]


if __name__ == '__main__':
    import random
    a = list(range(10))
    random.shuffle(a)
    print(a)
    arr = Selction_Sort(a)
    print('---'*10)
    print("實際執行次數：\t" + str(arr[1][0]+arr[1][1]+arr[1][2]))
    print("n^2:\t\t" + str(arr[1][2]))
    print("n:\t\t" + str(arr[1][1]))
    print("個位：\t\t" + str(arr[1][0]))
    print('---'*10)
    print("Big-O: n^2")
