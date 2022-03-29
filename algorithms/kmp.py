"""
[x]aababcxabcaabcabxabcabcx
[a]bcabcf -> lcps=0, match=0 -> starti+=1, startj=0

xa[a]babcxabcaabcabxabcabcx
 a[b]cabcf -> lcps=0, match=1 -> starti+=1, startj=0

xaab[a]bcxabcaabcabxabcabcx
  ab[c]abcf -> lcps=0, match=2 -> starti+=2, startj=0

xaababc[x]abcaabcabxabcabcx
    abc[a]bcf -> lcps=0, match=3 -> starti+=3, startj=0
    
xaababc[x]abcaabcabxabcabcx
       [a]bcabcf -> lcps=0, match=0 -> starti+=1, startj=0
    
xaababcxabca[a]bcabxabcabcx
        abca[b]cf -> lcps=1, match=4 -> starti+=3, startj=1
    
xaababcxabca[a]bcabxabcabcx
           a[b]cabcf -> lcps=0, match=1 -> starti+=1, startj=0
    
xaababcxabcaabcab[x]abcabcx
            abcab[c]f -> lcps=2, match=5 -> starti+=3, startj=2
    
xaababcxabcaabcab[x]abcabcx
               ab[c]abcf -> lcps=0, match=2 -> starti+=2, startj=0
    
xaababcxabcaabcab[x]abcabcx
                 [a]bcabcf -> lcps=0, match=0 -> starti+=1, startj=0
    
xaababcxabcaabcabxabcabc[x]
                  abcabc[f] -> lcps=3, match=6 -> starti+=3, startj=3
    
xaababcxabcaabcabxabcabc[x]
                     abc[a]bcf -> lcps=0, match=3 -> starti+=3, startj=0
    
xaababcxabcaabcabxabcabc[x]
                        [a]bcabcf -> lcps=0, match=0 -> starti+=1, startj=0

s     a b c a b c f
lcps  0 0 0 1 2 3 0
start 0 0 0 1 2 3 0 
"""

def getLCPS(s): # O(len(s))
    L, start  = [0], 0
    for i in range(1,len(s)):
        L.append( L[-1]+1 if s[i]==s[start] else 0 )
        start = start+1 if s[i]==s[start] else 0
    return L
getLCPS("abcabcf")
