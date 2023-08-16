def isBalanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return "NO"
        else:
            return "NO"

    return "YES" if not stack else "NO"

# Read input
n = int(input())  # Read the number of strings
for _ in range(n):
    s = input().strip()  # Read the string of brackets
    result = isBalanced(s)  # Call the isBalanced function
    print(result)  # Print the result (either YES or NO)