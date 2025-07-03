class Solution:
    def lexicalOrder(self, n):
        result = []
        curr = 1

        for _ in range(n):
            result.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10
                curr += 1

        return result
