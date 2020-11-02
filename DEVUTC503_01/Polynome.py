def P(l,n):
 if(len(l)==0): return 0
 else: return l[0]+ n*P(l[1:],n)
