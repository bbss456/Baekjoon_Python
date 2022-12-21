#그리드 알고리즘
# n값
# mod_val 나누기 값 얻기 값
mod_val=1
coin_list=[]

conin=1 # 시작 값
start=1 # 시작 값

n, k = map(int, input().split())
for i in range(n):
    coin_list.append(int(input()))

coin_len = len(coin_list) -1
count=0
count_hap=0
while(k>0):
    if(int(k/coin_list[coin_len])==0):
        coin_len -=1
    else:
        count = k//coin_list[coin_len]
        k=k-coin_list[coin_len]*count
        count_hap += count
print(count_hap)
