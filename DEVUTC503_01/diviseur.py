def diviseur(n):
   if(n>0):
      for i in range(2,n):
         if((n%i)==0):
            return i
         else:
            i=i+1
if __name__ == "__main__":
    print(diviseur(8))
    print(diviseur(9))