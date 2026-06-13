class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ''
        for string in s:
            if string.isalnum():
                news += string.lower()
        i = 0
        j = len(news) - 1
        while i < j:
            if news[i] == news[j]:
                i+=1 
                j-=1
            else:
                return False
        return True

        