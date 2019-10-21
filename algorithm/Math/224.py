'''
224. Basic Calculator
https://leetcode.com/problems/basic-calculator/

Hi, here's your problem today. This problem was recently asked by Google:
Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open ( and closing parentheses ), 
the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:
Input: "1 + 1"
Output: 2

Example 2:
Input: " 2-1 + 2 "
Output: 3

Example 3:
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
'''
from typing import *

# Approach 1: Stack and String Reversal
class Solution1:
    def evaluate(self, stack):
        # First operand, remove unnecessary ops
        result, fistSign = 0, 1
        while stack:
            result = stack.pop()
            if type(result) == int:
                result *= fistSign
                break
            # For negative operand
            # e.g. -1 + 1
            elif result == '-':
                fistSign = -1
        
        # Evaluate the expression till we get corresponding ')'
        while stack:
            op = stack.pop()
            if op == '+':
                result += stack.pop()
            elif op == '-':
                result -= stack.pop()
            elif op==')':
                break
        return result

    def calculate(self, s: str) -> int:
        stack = []
        operand, n = 0, 0

        # Put the elements of the expression into the stack from right to left.
        # Evaluation for the expression is done correctly from left to right!!
        for i in range(len(s)-1, -1, -1):
            char = s[i]
            
            # Use isdigit() to judge whether char is '0'~'9' or not
            if char.isdigit():
                # Forming the operand - in reverse order.
                operand += (10**n * int(char))
                n += 1
            
            elif char != ' ':
                if n:
                    # Save the operand on the stack
                    # As we encounter some non-digit.
                    stack.append(operand)
                    operand, n = 0, 0
                
                if char == '(':
                    res = self.evaluate(stack)
                    # Append the evaluated result to the stack.
                    # This result could be of a sub-expression within the parenthesis.
                    stack.append(res)
                else:
                    # For other non-digits just push onto the stack.
                    stack.append(char)
        
        # Push the last operand to stack, if any.
        if n:
            stack.append(operand)
        
        # Evaluate any left overs in the stack.
        return self.evaluate(stack)

# Approach 2: Stack and No String Reversal
# re-written expression would follow associativity rule
# e.g. A - B - C could be re-written as A+(−B)+(−C)
class Solution2:
    def calculate(self, s: str) -> int:
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative
        stack = []
        
        for c in s:
        
            if c.isdigit():
                # Forming operand, 
                # since it could be more than one digit
                operand = (operand * 10) + int(c)
            
            elif c == '+':
                # Evaluate the expression to the left
                res += sign * operand
                # Save '+' sign and Reset operand
                sign, operand = 1, 0
            
            elif c == '-':
                # Evaluate the expression to the left
                res += sign * operand
                # Save '-' sign and Reset operand
                sign, operand = -1, 0
            
            elif c == '(':
                # Push the sign and result on to the stack
                stack.append((sign, res))
                # Reset sign and Reset operand and Reset RESULT!!
                sign, operand, res = 1, 0, 0
            
            elif c == ')':
                # Evaluate the expression to the left
                res += sign * operand
                
                # (operand on stack) + (sign on stack * (result from parenthesis))
                (s, r) = stack.pop()
                res = r + s * res
                
                # Reset sign and Reset operand
                sign, operand = 1, 0
        
        return res + sign * operand

solutions = {
    'Solution 1' : Solution1(), 
    'Solution 2' : Solution2()
}
for key in solutions:
    print(key + ':')
    sol = solutions[key]
    
    print(sol.calculate("1 + 1"))
    #2
    print(sol.calculate(" 2-1 + 2 "))
    #3
    print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))
    #23
    print(sol.calculate("(+1+(+4+5+2)-3)+(+8)"))
    #17
    print(sol.calculate("+(1+(4+5+2)-3)+(+8)"))
    #17
    print(sol.calculate("+(-1+(4+5+2)-3)+(+8)"))
    #15
    print(sol.calculate("+(1+(4+5+2)-3)+(+8)+10(1)"))
    #Should be 18, we only have +, -, (, )
