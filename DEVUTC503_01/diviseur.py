def diviseur(n):
   if(n>0):
      for i in range(2,n):
         if((n%i)==0):
            return i
         else:
            i=i+1
