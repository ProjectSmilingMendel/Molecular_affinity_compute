#!/usr/bin/python3
def find_corresponding_parentheses(s):
    stack = []
    result = {}

    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if stack:
                result[stack.pop()] = i
            else:
                # Unmatched closing parenthesis
                result[i] = None

    # Any unmatched open parentheses
    for index in stack:
        result[index] = None

    return result

# Example
input_string = "CC(Oo(TH)o4)=O(7879=0w)(NN)"
corresponding_parentheses = find_corresponding_parentheses(input_string)
fragments = []
#for open_index, close_index in corresponding_parentheses.items():
#    print(f"({open_index}, {close_index})")
for open_index, close_index in corresponding_parentheses.items():
    a = ""
    for i in range(open_index+1,close_index):
        a = a + input_string[i]
    fragments.append(a)
