def check_parentheses(s):
    stack = []
    # Ánh xạ ngoặc đóng -> ngoặc mở
    mapping = {
	    ')': '(', 
	    ']': '[', 
	    '}': '{'
    }

    for char in s:
        if char in mapping.values():  # Nếu là dấu mở
            stack.append(char)
        elif char in mapping:  # Nếu là dấu đóng
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            return False

    return not stack  # Stack phải rỗng mới đúng

# TEST CASE
print(check_parentheses("(){}[]"))        # True Case 1
print(check_parentheses("([{}])"))        # True
print(check_parentheses("(]"))            # False
print(check_parentheses("({[})"))         # False

