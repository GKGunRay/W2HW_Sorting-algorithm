#20200930
#Bubble改成使用者輸入6個數字。
def Bubble_Sort(datas):
    for i in range(1, len(datas)):
        for j in range(len(datas)-i):
            if datas[j] > datas[j+1]:
                datas[j], datas[j+1] = datas[j+1], datas[j]
    return datas


if __name__ == '__main__':
    import random
    print("Please input 6 numbers:")
    a = list(range(6))
    for i in range(6):
        a[i] = int(input())
    print(a)
    a = Bubble_Sort(a)
    print(a)
