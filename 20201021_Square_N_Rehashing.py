# 20201021
import random
#目標：平方探測法、再雜湊法
#共通
INDEXBOX = 10    #雜湊表最大元素
MAXNUM = 7       #最大資料個數

def print_data(data, max_number):  #列印陣列副程式
    print('\t', end='')
    for i in range(max_number):
        print('[%2d] ' %data[i], end = '')
    print()
   
#線性探測法
def create_table_linear(num, index):  #建立雜湊表副程式
    tmp = num % INDEXBOX       #雜湊函數=資料 % INDEXBOX
    while True:
        if index[tmp] == -1:   #如果資料對應位置是空的
            index[tmp] = num   #則直接存入資料
            break
        else:
            tmp = (tmp + 1) % INDEXBOX #否則往後找位置存放

#平方探測法
def create_table_square(num, index):  #建立雜湊表副程式
    collision_times = 0
    tmp = num % INDEXBOX       #雜湊函數=資料 % INDEXBOX
    while True:
        if index[tmp] == -1:   #如果資料對應位置是空的
            index[tmp] = num   #則直接存入資料
            break
        else:
            #collision
            collision_times += 1
            tmp = (num + collision_times ** 2) % INDEXBOX #否則add (collision times) ^ 2

#再雜湊法
def create_table_rehashing(num, index):  #建立雜湊表副程式
    collision_times = 0
    tmp = num % INDEXBOX       #雜湊函數=資料 % INDEXBOX
    while True:
        if index[tmp] == -1:   #如果資料對應位置是空的
            index[tmp] = num   #則直接存入資料
            break
        else:
            #collision
            collision_times += 1
            tmp = (num + collision_times * 2) % INDEXBOX #否則add 2*(collision times)

         

#Main
index = [None]*INDEXBOX
data = [None]*MAXNUM

print('陣列原始值：')
for i in range(MAXNUM):    #起始資料值
    data[i] = random.randint(1, 20) #隨機生成資料
print_data(data, MAXNUM)   #列印起始資料

#線性探測法
for i in range(INDEXBOX):   #清除雜湊表
    index[i] = -1          #（初始化雜湊表）
print('\n' + '---'*10 + '\n線性探測法\n' + '---'*10)
print('雜湊表內容：')
for i in range(MAXNUM):    #建立雜湊表
    create_table_linear(data[i], index)
    print('  %2d =>' % data[i], end='') #列印單一元素的雜湊表位置
    print_data(index, INDEXBOX)

print('完成雜湊表：')
print_data(index, INDEXBOX) #列印最後完成Result

#平方探測法
for i in range(INDEXBOX):   #清除雜湊表
    index[i] = -1          #（初始化雜湊表）
print('\n' + '---'*10 + '\n平方探測法\n' + '---'*10)
print('雜湊表內容：')
for i in range(MAXNUM):    #建立雜湊表
    create_table_square(data[i], index)
    print('  %2d =>' % data[i], end='') #列印單一元素的雜湊表位置
    print_data(index, INDEXBOX)

print('完成雜湊表：')
print_data(index, INDEXBOX) #列印最後完成Result

#再雜湊法
for i in range(INDEXBOX):   #清除雜湊表
    index[i] = -1          #（初始化雜湊表）
print('\n' + '---'*10 + '\n再雜湊法\n' + '---'*10)
print('雜湊表內容：')
for i in range(MAXNUM):    #建立雜湊表
    create_table_rehashing(data[i], index)
    print('  %2d =>' % data[i], end='') #列印單一元素的雜湊表位置
    print_data(index, INDEXBOX)

print('完成雜湊表：')
print_data(index, INDEXBOX) #列印最後完成Result

#平方探測法Main
