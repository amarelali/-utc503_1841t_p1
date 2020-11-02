def factorial(n):
   res = 1
   while n >= 1:
      res = res * n
      n = n - 1
   return res
if __name__ == "__main__":
    print(factorial(3))