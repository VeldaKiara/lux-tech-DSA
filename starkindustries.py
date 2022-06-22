'''
Constraints: time is unidirectional, buy then sell in future, buy low, sell high
create a func
Use two pointers, left to 0 and right 1, left-> buy, right-> sell
while  loop the right pointer is less than len of prices
check for profit: - 
                left prices < right,
                 right-left = profit, 
                 max profit= max(max, profit) 
                 else left = right, move left all the way to right, 
                 due to low price, left= lowest/minimum
                 increment the right 
return max profit
'''
def maxProfit(prices):
    left, right = 0, 1 
    max_profit = 0 
    while right < len(prices):
        #check if profitable
        if prices[ left] < prices [ right]:
            profit = prices[right] - prices [ left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1
    return max_profit
    
print(maxProfit([7,1,5,3,6,4])) #5
            
           