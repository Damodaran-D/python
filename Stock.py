import sys

def stockmax(prices):
    # Complete this function
    buy=0
    cost=0
    profit=0
    m=max(prices)
    l=len(prices)
    for i in range(l):        
        if prices[i]!=m:
            buy+=1
            cost+=prices[i]
        elif prices[i]==m:
            if i!=l-1:
                m=max(prices[i+1:])
            profit+=(prices[i]*buy-cost)
            buy=0
            cost=0
        #print("m:"+str(m))
    return profit
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        prices = list(map(int, input().strip().split(' ')))
        result = stockmax(prices)
        print(result)
