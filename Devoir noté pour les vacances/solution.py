#1 list est le solution optimal
#2.1
def rendreMonnaieRec(list , monnaie):
    listRendu = []
    if list == [] :
        print("pas de monnaie a rendu")
    else:            
            n = monnaie / list[0]
            listRendu.append(int(n))
            monnaie = (monnaie - list[0])
            return listRendu + rendreMonnaie(list[1:] , monnaie)
        
            
#2.2
# def rendreMonnaieListComp(list , monnaie):
#     listRendu = []
#     obj = [if list == [] print("pas de monnaie a rendu") else for x in list n = monnaie / x listRendu.append(int(n))  monnaie = (monnaie - x) return  listRendu ]
#     print(obj)
#2.3
def rendreMonnaie(list , monnaie):
    listRendu = []
    if list == [] :
        print("pas de monnaie a rendu")
    else:
        for x in list :
            
            n = monnaie / x
            listRendu.append(int(n))
            monnaie = (monnaie - x)
        return  listRendu
            
print(rendreMonnaie([5000 , 2000] , 7000))
print(rendreMonnaieRec([5000 , 2000] , 7000))

print(rendreMonnaie([5000 , 3000] , 7000))
print(rendreMonnaieRec([5000 , 3000] , 7000))

#3

# def toutRendreMonnaie(list , monnaie):
#     toutRendreMonnaie =[]
#     l=[]
#     toutRendreMonnaie.append(rendreMonnaie(list , monnaie))
#     for x in toutRendreMonnaie:
#          for i in range(0,len(x)):
#             print(toutRendreMonnaie.append(rendreMonnaie(l[i] , monnaie)))
#     return toutRendreMonnaie
# print(toutRendreMonnaie([5000 , 1000] , 7000))



