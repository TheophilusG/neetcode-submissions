class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operators = ['+','-', '*', '/']
        current_result = 0

        if len(tokens)==1: 
            return int(tokens[0])
        for opr in tokens:
            if opr in operators:
                operator_string = opr

                if stack and len(stack)>=2:
                    operand1= stack.pop()
                    operand2= stack.pop()
                    current_result = int(eval(f"int({operand1}) {operator_string} int({operand2})"))
                    stack.append(current_result)
            else:
                stack.append(opr)
        
        return int(current_result)


        