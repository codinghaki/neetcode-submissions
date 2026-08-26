class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Input: int[] nums
            - 2 <= nums.length <= 100,000
            - -30 <= nums[i] <= 30
        Process: For each index find product of all elements other than current index
        Output: Array of each process
            - Any product is guaranteed 32 bit int

        Eg1  [1,2,4,6] -> [2*4*6, 1*4*6, 1*2*6, 1*2*4] -> [48, 24, 12, 8]
        Pre  [1,1,2,8] *first index value is 1
        Post [48,24,6,1] *last index value is 1
        Then multiply pre post arrays

        Eg2 [-1,0,1,2,3] -> [0,-6,0,0,0]
        Pre [1,-1,0,0,0]
        Post[0,6,6,3,1]

        Brute force: For each index multiply everything on left by everything on right non-inclusive
        Idea: Brute force we are checking information we already know. How to store? Find pre and post product and mulitply
        '''
        # Iterate forward creating prefix array
        prefixArray = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            # First index is always 1
            if i == 0:
                prefixArray[i] = 1
            # pre[i] = pre[i - 1] * nums[i - 1]
            else:
                prefixArray[i] = prefixArray[i - 1] * nums[i - 1]
        # Iterate backward creating postfix array
        postfixArray = [1 for _ in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            # Last index is always 1
            if i == (len(nums) - 1):
                postfixArray[i] = 1
            # post[i] = post[i + 1] * nums[i + 1]
            else:
                postfixArray[i] = postfixArray[i + 1] * nums[i + 1]
        # Multiply pre and post and return
        answer = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            answer[i] = prefixArray[i] * postfixArray[i]
        return answer