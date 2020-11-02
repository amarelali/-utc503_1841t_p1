from math import sqrt
a=eval(input("entrer valeur de a:"))
b=eval(input("entrer valeur de b:"))
c=eval(input("entrer valeur de c:"))
d=pow(b,2)-4*a*c

if(a==0):
   print("c'est une equation du premier degre est la solution x=",-c/b)
else:
   if d<0:
      print("pas de solution dans R ")
   else:
      if d==0:
         print("la solution est x'=x''""",-b/(2*a))
      else:
         if d>0:
            print("Il admet 2 solutions x'=",(-b-sqrt(d))/(2*a),"et",(-b+sqrt(d))/(2*a))
