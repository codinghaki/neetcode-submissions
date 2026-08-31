class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Input: int[] nums
        Task: Find length of longest consecutive sequence amongst elements
            Sequence=each element 1 greater
            MUST WRITE IN O(n)
        Output: Return length of longest consecutive sequence

        Eg1 [2,20,4,10,3,4,5]
        4 = 2,3,4,5

        2,3,4,5|10|20

        Eg2 [0,3,2,5,4,6,1,1]
        7 = 0,1,2,3,4,5,6

        Brute force: For each number check if +1 then +1 then +1 

        Notes:
        - How can we be more efficient? Why keep checking +1 if we've already seen
        '''
        # Create set from nums
        unique = set(nums)
        # Iterate through nums
        longest = 0
        for num in nums:
            # If num - 1 in set, continue
            if (num - 1) in unique:
                continue
            # Else if not, that means start of sequence
            else:
                currentSequence = 1
                currentNum = num
                # Keep track of longest sequence
                while currentNum in unique:
                    longest = max(currentSequence, longest)
                    currentSequence += 1
                    currentNum += 1
        # return longest
        return longest