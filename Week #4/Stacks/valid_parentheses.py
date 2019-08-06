class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for i in s:
            if(i == "("):
                #push
                stack.append("(")
            elif(i == "["):
                #push
                stack.append("[")

            elif(i == "{"):
                #push
                stack.append("{")
            elif(len(stack) > 0 and stack[-1] == "(" and i == ")"):
               #pop
                stack.pop(-1)
            elif(len(stack) > 0 and stack[-1] == "[" and i == "]"):
                #pop
                stack.pop(-1)
            elif(len(stack) > 0 and stack[-1] == "{" and i == "}"):
                #pop
                stack.pop(-1)
            else:
                stack.append(i)
        return len(stack) == 0
