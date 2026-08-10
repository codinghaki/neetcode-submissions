class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create counter for s
        sCharCount = Counter(s)
        # Create counter for t
        tCharCount = Counter(t)
        # Compare, if equal return True
        if sCharCount == tCharCount:
            return True
        # Else return False
        else:
            return False