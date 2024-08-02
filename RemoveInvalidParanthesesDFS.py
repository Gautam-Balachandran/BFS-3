# Time Complexity : O(n*2^n), where n is the average size of the string
# Space Complexity : O(n*2^n), for recursive stack space
class Solution:
    def __init__(self):
        self.result = set()  # Use a set to avoid duplicates

    def removeInvalidParentheses(self, s):
        if not s:
            return list(self.result)
        # Start the DFS removal process
        self.remove(s, 0, 0, ['(', ')'])
        return list(self.result)

    def remove(self, s, last_i, last_j, valid):
        # Count to keep track of the balance between parentheses
        count = 0
        for i in range(last_i, len(s)):
            if s[i] == valid[0]:
                count += 1  # Increment count for opening parenthesis
            if s[i] == valid[1]:
                count -= 1  # Decrement count for closing parenthesis
            if count >= 0:
                continue  # Continue if the count is non-negative

            # If the balance is negative, try removing a closing parenthesis
            for j in range(last_j, i + 1):
                # Ensure we remove only the first invalid closing parenthesis
                if s[j] == valid[1] and (j == last_j or s[j - 1] != valid[1]):
                    # Recursively call remove with the new string
                    cur = s[:j] + s[j + 1:]
                    self.remove(cur, i, j, valid)
            return  # Return after processing the current level

        # Reverse the string to check the other type of parenthesis
        reversed_s = s[::-1]
        if valid[0] == '(':
            # Call remove with reversed string and swapped parentheses
            self.remove(reversed_s, 0, 0, [')', '('])
        else:
            # Add the valid string to the result set
            self.result.add(reversed_s)

# Examples to test the code
sol = Solution()

# Example 1
example1 = "()())()"
print("Input:", example1)
print("Output:", sol.removeInvalidParentheses(example1)) # Output : ['()()()', '(())()']

# Example 2
example2 = "(a)())()"
sol = Solution()  # Reset the solution for a fresh result set
print("Input:", example2)
print("Output:", sol.removeInvalidParentheses(example2)) # Output : ['(a)()()', '(a())()']

# Example 3
example3 = ")("
sol = Solution()  # Reset the solution for a fresh result set
print("Input:", example3)
print("Output:", sol.removeInvalidParentheses(example3)) # Output : ['']