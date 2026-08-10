class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         appeared = set()

         for number in nums:
            if number in appeared:
                return True
            else:
                appeared.add(number)

         return False