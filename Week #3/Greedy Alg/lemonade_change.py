from collections import defaultdict
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        #have a count of the amount of 5s
        #have a current total
        #have a count for the amount of 20s?
        
        if the current bill is gather than 5
            calc change = bill - 5
            amount of fives = current total - 
            if not enough change (total - change < 0 or amount of five == 0)
                return false
            if bill == 20 and (amount of 5 < 3 and total < 15):
                return false
            if bill == 20
                num = current total - amount of fives * 5
                if(num >= 10 and amount of fives >= 1)
                    amount of 5s -= 1
                    count for 20 += 1
                    current total -= 15
                if(num < 10 and amount of fives >= 3):
                    amount of 5s -=3
                    current total -= 15
                    count for 20 += 1
                if(num < 10 and amount of fives < 3):
                    return false
                    
            if bill == 10 and (amount of 5 < 1):
                return false
            else:
                amount of 5 -= 1
                total -= 5
                total += bill
        if bill == 5:
            ammount of 5 += 1
            total += bill
        return true after all bills
        """
        amountFives = 0
        currentTotal = 0
        currentTwenties = 0
        for i in bills:
            if(i > 5):
                change = i - 5
                if(currentTotal - change < 0 or amountFives <= 0):
                    return False
                if(i == 20):
                    leftover = currentTotal - (amountFives * 5)
                    if(leftover >= 10 and amountFives >= 1):
                        amountFives -= 1
                        currentTwenties += 1
                        currentTotal -= change
                    if(leftover < 10 and amountFives >= 3):
                        amountFives -= 3
                        currentTwenties += 1
                        currentTotal -= change
                    if(leftover < 10 and amountFives < 3):
                        return False
                if(i == 10 and amountFives < 1):
                    return False
                if(i == 10 and amountFives >= 1):
                    amountFives -= 1
                    currentTotal -= change
                    currentTotal += i
            else:
                amountFives += 1
                currentTotal += i
        return True
                    
            
