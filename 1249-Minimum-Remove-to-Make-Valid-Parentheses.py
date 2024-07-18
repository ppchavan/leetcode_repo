class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if s == "":
            return s
        
        l_count, r_count = 0, 0
        valid_str = []

        # First pass for building valid string
        for ch in s:
            if ch == "(":
                l_count += 1
                valid_str.append(ch)
            elif ch == ")":
                if l_count > r_count:
                    r_count += 1
                    valid_str.append(ch)
            else:
                valid_str.append(ch)
        
        # If left and right parantheses are balanced, join all characters and return valid string
        if l_count == r_count:
            return "".join(valid_str)
        
        # Second pass: If left and right parantheses are not balanced, l_count must be greater than r_count, so we have to remove extra left parantheses. Before returning, we have to reverse the result.
        res = []
        
        # Iterate backwards
        for curr_char in reversed(valid_str):
            if curr_char == "(":
                if l_count <= r_count:
                    res.append(curr_char)
                else:
                    # Don't add the left parantheses to result string; l_count needs to be reduced
                    l_count -= 1
            else:
                # Alphabetical characters and right parantheses are added unconditionally
                res.append(curr_char)

        return "".join(reversed(res))

# Worst case time complexity is O (2N) ~ O(N) so its linear time complexity
# Space complexity O(N)