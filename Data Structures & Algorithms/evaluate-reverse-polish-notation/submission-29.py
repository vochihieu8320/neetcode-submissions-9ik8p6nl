class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        number_stack = []

        operators = ["+", '-', "*", "/"]
        for i in range(len(tokens)):
            character = tokens[i]
            if character not in operators:
                # this is number
                number_stack.append(character)
            else:
                # pop two element
                num_b = number_stack.pop()
                num_a = number_stack.pop()
                result = 0
                match character:
                    case "+": 
                        result = (int(num_a) + int(num_b))
                    case "-": 
                        result += (int(num_a) - int(num_b))
                    case "*": 
                        result = (int(num_a) * int(num_b))
                    case "/": 
                        result = (int(num_a) / int(num_b))

                number_stack.append(result)                

        print("number_stack", number_stack)
        return int(number_stack[-1])

            