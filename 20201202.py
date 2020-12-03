#20201202
from functools import cmp_to_key

# Q1
# 目標：輸入金額來print貪婪法的步驟
def giveChange(qt, change):
    coins = [0 for _ in range(len(qt))]
    for i, money in enumerate(qt):
        # 每一次貪婪法步驟
        coins[i] = int(change / money)
        change = change % money
        print("Step " + str(i+1) + ":", coins, change)



# Q2
# 目標：輸入金額來print動態規劃的步驟
def coin_change(coins, change, dp, coins_used):
    '''利用動態規劃求解找零需要的硬幣數，以及硬幣的使用情況'''
    for i in range(1, change+1):
        # 依次求解，dp[1] ~ dp[change]
        for j in range(len(coins)):
            if (coins[j] <= i):
                # 使用硬幣的前提：硬幣的額度 <= 需要找零的金額。
                # 比如：找零8元，不能使用10元硬幣
                if (dp[i-coins[j]]+1 < dp[i]):
                    #dp[i] = min(dp[i], dp[i-coins[j]]+1)
                    dp[i] = dp[i-coins[j]]+1
                    # 記錄使用的硬幣
                    new_coin = coins[j]
        coins_used[i] = new_coin
 
    if (dp[change] > change):
        #無解的情況，初始化的时候設置dp[change] = change+1
        return -1
    else:
        return dp[change]



# Q3
# 目標：用限重背包偷取最大價值東西的貪婪法步驟
def fractional_backpack(goods, w):
    # w 表示背包的限重
    # m 表示每個商品拿走多少個
    total_v = 0
    m = [0 for _ in range(len(goods))]
    for i, (weight, price, name) in enumerate(goods):
        # 因為已依照最大價值重量比排列list，可以直接使用貪婪法
        if w >= weight:
            m[i] = 1
            w -= weight
            total_v += price
        print("Step " + str(i+1) + ":", m, w, "| Total value:", total_v)



# Q4
# 目標：用限重背包偷取最大價值東西的動態規劃步驟
# 備註：可以用「價值/重量」比作為偷取優先度的基準？
def used_coins(change, used_coins):
    '''利用used_coins求使用的硬幣'''
    re=[]
    i = 0
    while change:
        #dp[i]= dp[i-coins[j]]+1    used_coins[change]=coins[j]
        tmp = used_coins[change]
        re.append(tmp)
        change -= tmp
        i += 1
        print("Step " + str(i) + ": take the", tmp, "dollar coin.")
    return re

def MaxVal2(memo, w, v, index, last):  
    """ 
    得到最大價值 
    w為widght 
    v為value 
    index為索引 
    last為剩餘重量 
    """  

    global numCount  
    numCount = numCount + 1  

    try:  
        #以往是否計算過分支，如果計算過，直接返回分支的結果  
        return memo[(index , last)]  
    except:  
        #最底部  
        if index == 0:  
            #是否可以裝入  
            if w[index] <= last:
                return v[index][1] 
            else:  
                return 0  

        #尋找可以裝入的分支  
        without_l = MaxVal2(memo , w, v, index - 1, last)  

        #如果當前的分支大於約束  
        #返回歷史查詢的最大值  
        if w[index] > last:  
            return without_l  
        else:  
            #當前分支加入背包，剪掉背包剩餘重量，繼續尋找  
            with_l = v[index][1] + MaxVal2(memo , w, v , index - 1, last - w[index])  

        #比較最大值  
        maxvalue = max(with_l , without_l)
        print("[The", str(numCount)+"th search]")
        print("Find the max value item: " + v[index][0])
        print("Current total value:", maxvalue)
        #儲存  
        memo[(index , last)] = maxvalue  
        return maxvalue  



 
if __name__=='__main__':
    # Q1 & 2
    quota = [25, 20, 5, 1]
    
    change = int(input("Q1: How much money would you like to get change? "))
    print()
    print("-"*50 + "\nGreedy Method:\n")
    giveChange(quota, change)

    print()
    print("-"*50 + "\nDynamic Programming:\n")
    dp = [change+1]*(change+1)
    dp[0] = 0
    coins_used = [0]*(change+1)
    re = coin_change(quota, change, dp, coins_used)
    re_coins = used_coins(change, coins_used)
    print("For the change of {0}-dollar(s), {1} coin(s) are needed: {2}\n".format(change, re, re_coins))


    print("="*50)
    print("="*50)

    # Q3 & 4
    w = [0, 5, 1, 4, 3, 2]   # 東西的重量
    # 東西的價值
    v = [["", 0],\
         ["PS5", 17000],\
         ["iPad pro 12", 35000],\
         ["Macbook pro 15", 60000],\
         ["HomePod", 9000],\
         ["Mac mini", 20000]]
    #  $3400/kg
    # $35000/kg
    # $15000/kg
    #  $3000/kg
    # $10000/kg
    goods = []
    x = 0
    while x < len(w):
        goods.append((w[x], v[x][1], v[x][0]))
        x += 1
    goods.pop(0)
    
    m = int(input("Q2: How many kilograms can your backpack afford? "))
    print()
    print("-"*50 + "\nGreedy Method:\n")
    # 每個商品元組表示（價格，重量）
    fractional_backpack(goods, m)
    
    print()
    print("-"*50 + "\nDynamic Programming:")
    numCount = 0  
    memo = {} 
    n = len(w) - 1
    print()
    print("\nMax value: " + str(MaxVal2(memo , w, v, n, m)) + "; caculate times:", numCount)


