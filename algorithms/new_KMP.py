class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        i = 0
        while True:
            while len(haystack)-i>=len(needle) and haystack[i]!=needle[0]:
                i+=1
            if len(haystack)-i<len(needle):
                return -1
            
            #print('S', i)
            i, j, lcps = i+1, 1, 0
            while j<len(needle) and haystack[i]==needle[j]:
                if haystack[i-j+lcps]==haystack[i]:
                    lcps+=1
                i, j = i+1, j+1
            #print('E', i, j, lcps, '\n')

            if j==len(needle):
                return i-j
            i = i-lcps
