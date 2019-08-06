class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        
        """
        
        #creating a postfix string 
        stack = []
        total = []
        for i in S:
            if i == "(":
                stack.append("(")
            #if the there is a closing bracket and the top number is not ( then we multiply
            if i == ")" and stack[-1] != "(":
                nums = stack.pop(-1)
                stack.pop(-1)
                stack.append(nums)
                total.append("*")
            #if there is a closing bracket and the top number is a ( then we know it is a 1
            if i == ")" and stack[-1] == "(":
                stack.pop(-1)
                stack.append(1)
                total.append("1")
            #if the top 2 are numbers then we know we need to add
            if len(stack) > 1 and stack[-1] != "(" and stack [-2] != "(":
                stack.pop(-1)
                total.append("+")
            
                
            
            
        #calculating the post fix
        currentTotal = 0
        result = []
        for i in total:
            if(i == "1"):
                result.append(1)
            elif(i == "*"):
                num = result.pop(-1)
                result.append(num * 2)
            else:
                num = result.pop(-1)
                num2 = result.pop(-1)
                result.append( num + num2)
            
        return result[0]
            
