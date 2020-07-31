#-------------------------------------GITHUB REPOSITORY LINK---------------------------

from collections import defaultdict
import sys
def Calc_SubString (S):
  distinct = len(set(list(S)))
  num = len(S)
  frequency = defaultdict(int)
  index = 0
  min_len = sys.maxsize
  distinct_till_here = 0 
  for j in range(num):
    frequency[S[j]] += 1
    if frequency[S[j]] == 1:
      distinct_till_here += 1
    
    if distinct == distinct_till_here:
      while frequency[S[index]] > 1:
        if frequency[S[index]] > 1:
          frequency[S[index]] -= 1
        index += 1
      
      curr_len = j - index + 1
      min_len = min(min_len, curr_len)
  return min_len
 
 
    
 
S = input()
 
out_ = Calc_SubString(S)
print (out_)
