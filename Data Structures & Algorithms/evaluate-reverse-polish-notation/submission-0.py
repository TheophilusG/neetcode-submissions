class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operators = ['+','-', '*', '/']
        current_result = 0

        for opr in tokens:
            if opr in operators:
                operator_string = opr

                if stack and len(stack)>=2:
                    operand1= stack[-1]
                    operand2= stack[-2]
                    current_result = eval(f"int({operand1}) {operator_string} int({operand2})")
            else:
                stack.append(opr)
        
        return current_result


        