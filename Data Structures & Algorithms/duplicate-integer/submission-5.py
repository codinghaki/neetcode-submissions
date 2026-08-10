class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a set 'seen'
        seenNumbers = set()
        # Iterate through nums
        for num in nums: # O(n) time + space
            # Check if number is in set, if yes return True
            if num in seenNumbers:
                return True
            # Else, add it to set and keep iterating
            else:
                seenNumbers.add(num)
        # If reached end of list we know no repeats
        return False