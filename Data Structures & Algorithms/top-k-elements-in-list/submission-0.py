class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''Input: Int[] nums, int k
        # k can be any number within range of array
        # Process: Find k most frequent elements, can return in any order

        Example 1: 1 1s, 2 2s, 3 3s
        Example 2: 2 7s

        Own example: [1,2,3,4,5] and k=5 then return [1,2,3,4,5]

        Brute force: Iterate through taking count, sort, return k top
        Solution?: Take count, map frequency to array, iterate down
        '''
        # Take frequency of each num
        numsFrequency = {}
        for num in nums:
            numsFrequency[num] = numsFrequency.get(num, 0) + 1
        # Create array length of nums
        frequenciesArray = [[] for _ in range(len(nums) + 1)]
        # To array assign index using frequency
        for number, frequency in numsFrequency.items():
            frequenciesArray[frequency].append(number)
            print(number, frequency)
        # Iterate backwards if length of return list == k return
        answer = []
        for i in range(len(frequenciesArray) - 1, -1, -1):
            for number in frequenciesArray[i]:
                answer.append(number)
            if len(answer) == k:
                return answer
        return answer