class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Input: int[] temperatures
            - temperatures[i] == daily temp on ith day
        Task: For each day, find number of days until warmer temp appears
            - If no warmer day in future, result[i] == 0
        Output: Return results array int[]

        [30,38,30,36,35,40,28]
        [1, 4, 1, 2, 1, 0, 0]

        30 -> [(30,0)]
        38 -> 
        Pop 30, index 0 becomes (1 - 0)
        [(38,1)]
        30 -> [(38,1),(30,2)]
        36 -> Pop 30, index 2 becomes 2 - 1
        [(38,1),(36,3)]
        35 -> [(38,1),(36,3),(35,4)]
        40 ->
        Pop 35, index 4 becomes (5 - 4)
        Pop 36, index 3 becomes (5 - 3)
        Pop 38, index 1 becomes (5 - 1)
        [(40,5)]
        28 -> [(40,5),(28,6)]
        Just initialise results with 0's?

        [22,21,20]
        22...:0
        21...:0
        20...:0

        Brute force: For each index keep iterating until larger number found
        Notes: We shouldn't have to keep iterating when we've seen values before
        Optimal: Use stack to keep track of when we see hotter day?
        '''
        # Initialise results with 0s
        results = [0 for _ in range(len(temperatures))]
        # Initialise Stack
        stack = []
        # Iterate through index, temp in temps
        for index, temp in enumerate(temperatures):
            # While stack and currentTemp > stack.peek()
            while stack and temp > stack[-1][0]:
                # Pop top temp
                poppedTemp, poppedIndex = stack.pop()
                # Popped tempIndex == currentIndex - tempIndex
                results[poppedIndex] = (index - poppedIndex)
            # Add current (temp, index) to stack
            stack.append((temp,index))
        # return results
        return results
        