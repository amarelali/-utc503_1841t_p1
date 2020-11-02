def P(l,n):
 if(len(l)==0): return 0
 else: return l[0]+ n*P(l[1:],n)
if __name__ == "__main__":
    print(P([1, 5, 3] , 2))
