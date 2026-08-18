class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a counter for each word
        def createCharCounter(word:string):
            # Create array
            charArray = [0] * 26
            # Iterate through chars in word
            for char in word:
                # Increment letter count
                charArray[ord(char) - ord('a')] += 1

            return tuple(charArray)

        # One element, always return single sublist
        if len(strs) == 1:
            return [[strs[0]]]

        # Maintain Hashmap<Array, List>
        groupedAnagrams = {}
        # Iterate through words
        for word in strs:
            # Create counter
            currentWordCounter = createCharCounter(word)
            # Add to sublist
            if currentWordCounter in groupedAnagrams:
                groupedAnagrams[currentWordCounter].append(word)
            else:
                groupedAnagrams[currentWordCounter] = [word]
    
        # Iterate through hashmap and collate lists
        return [anagramList for anagramList in groupedAnagrams.values()]