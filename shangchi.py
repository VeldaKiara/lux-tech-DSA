class Solution:
    def isValid(self, s):
        openingBrackets = "({["
        closingBrackets = ")}]"
        matchingBrackets = { ")":"(", "}":"{", "]":"["}
        stack = [ ]
        
        for bracket in s:
            if bracket in openingBrackets:
                stack.append(bracket)
            elif bracket in closingBrackets:
                if len(stack) == 0:
                    return False
                if stack[-1] == matchingBrackets[bracket]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
            