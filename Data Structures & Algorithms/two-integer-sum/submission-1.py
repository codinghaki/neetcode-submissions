class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create Hashmap<Value, Index>
        seenNumbers = {}
        # Enumerate through nums
        for currentIndex, num in enumerate(nums):
            # If target - num in seen
            if (target - num) in seenNumbers:
                # Return [value[target-num], index]
                complimentIndex = seenNumbers[target - num]
                return [complimentIndex, currentIndex]
            # Else
            else:
                # Add to hashmap[value] = index
                seenNumbers[num] = currentIndex