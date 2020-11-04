#20201104_HanoiTower

#hanoi(Layer, Start, Temp, End)
def hanoi(n, A, B, C):
    if n == 1:
        return [(A, C)]
        # 只剩下1層時只由A移到C。
    else:
        return hanoi(n-1, A, C, B) + hanoi(1, A, B, C) + hanoi(n-1, B, A, C)
        

n = input("請輸入漢諾塔層數：")
movecount = 0
for move in hanoi(int(n), 'A', 'B', 'C'):
    #Output of hanoi(n, A, B, C): [(,),(,),...][(,),(,),...]
    movecount += 1
    print(("%c --> %c，移動次數："+str(movecount)) % move)


