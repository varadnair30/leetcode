class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words=s.split()
        maxi=float('-inf')
        for char in words:

            if char.isdigit():
                if maxi>=int(char):
                    return False
                maxi=int(char)
        return True







            


        