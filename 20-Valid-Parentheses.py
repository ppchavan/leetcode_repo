class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        
        # Create a map of closing to opening braces for quick lookup.
        m = {
            \)\: \(\,
            \]\: \[\,
            \}\: \{\
             }
        
        stack = []
        for ch in s:
            if ch in [\(\, \{\, \[\]:
                stack.append(ch)
            else:
                if not stack:
                    return False
                
                top = stack[-1]
                # If top character in stack is matching the closing bracket, pop the top char.
                if ((ch == ')' and top == m[ch]) or
                (ch == ']' and top == m[ch]) or
                (ch == '}' and top == m[ch])):
                    stack.pop()
                else:
                # If the previous condition is false, we have invalid string. So we can return False early.
                    return False;
        
        # String is valid only if stack is empty.
        return not stack

# Time complexity is O(N), where N is length of string
# Space complexity is O(N)