class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter

        # count frequency of the each character
        freq = Counter(s)

        # listss to hold frequencies based on odd/even
        odd_freqs = []
        even_freqs = []

        # seperating them
        for count in freq.values():
            if count % 2 == 1:
                odd_freqs.append(count)
            else:
                even_freqs.append(count)

        # If either list is empty, return -1 
        if not odd_freqs or not even_freqs:
            return -1

        # Find maximum difference
        return max(odd_freqs) - min(even_freqs)
