# Time Complexity : O(n*2^n), where n is the average size of the string
# Space Complexity : O(n*2^n), for the set and queue
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s):
        if s is None or len(s) == 0:
            return []

        result = []
        visited = set()
        queue = deque([s])
        valid = False
        visited.add(s)

        while queue:
            sub_str = queue.popleft()  # Dequeue the next expression

            if self.is_valid(sub_str):  # Check if the current expression is valid
                result.append(sub_str)
                valid = True

            if valid:
                continue  # If we've found a valid expression, don't explore further

            for i in range(len(sub_str)):
                # Only consider removing '(' or ')'
                if sub_str[i] == '(' or sub_str[i] == ')':
                    # Generate a new expression by removing the current
                    # character
                    cur = sub_str[:i] + sub_str[i + 1:]

                    if cur not in visited:  # If this new expression hasn't been visited
                        queue.append(cur)
                        visited.add(cur)

        return result

    def is_valid(self, s):
        count = 0

        for c in s:
            if c == '(':
                count += 1
            if c == ')':
                count -= 1
            if count < 0:
                return False

        return count == 0

# Examples

# Example 1
s = "()())()"
solution = Solution()
print(solution.removeInvalidParentheses(s)) # Output : ["()()()", "(())()"]

# Example 2
s = "(a)())()"
solution = Solution()
print(solution.removeInvalidParentheses(s)) # Output : ["(a)()()", "(a())()"]

# Example 2
s = ")("
solution = Solution()
print(solution.removeInvalidParentheses(s)) # Output : [""]