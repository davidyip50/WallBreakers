class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        ["5","2","C","D","+"]
        sum = 5 7 5 15 30
        5
        10
        
        ["5","-2","4","C","D","9","+","+"]
        sum = 5 3 7 3 -1 8 13 27
        5
        -2
        -4
        9
        5
        """
        total = 0
        top = 0
        stack = []
        
        for i in ops:
            if(i == "C"):
                #pop and subtract top
                total -= stack[-1]
                stack.pop(-1)
            elif(i == "D"):
                #double the top and push
                total += int(stack[-1]) * 2
                stack.append(int(stack[-1]) * 2)
            elif(i == "+"):
                #add the top two
                addTop = int(stack[-1]) + int(stack[-2])
                total += addTop
                stack.append(addTop)
            else:
                total += int(i)
                stack.append(int(i))
        return total
