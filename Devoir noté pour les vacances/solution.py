#1 list est le solution optimal
#2.1
def rendreMonnaieRec(list , monnaie):
    listRendu = []
    if list == [] :
        return listRendu
    else:            
            n = monnaie / list[0]
            listRendu.append(int(n))

            monnaie = (monnaie - list[0])
            return listRendu + rendreMonnaieRec(list[1:] , monnaie)
        
            
#2.2
# def rendreMonnaieListComp(list , monnaie):
#     listRendu = []
#     obj = [if list == [] print("pas de monnaie a rendu") else for x in 

#list n = monnaie / x listRendu.append(int(n))  monnaie = (monnaie - x) 

#return  listRendu ]
#     print(obj)
# def rendreMonnaieListComp(list , monnaie):
#       list2 = []
#          list2 = [ 0 if x == 0  else  int(monnaie / x ) monnaie - x   for x in list ]  
#          return list2

# print(rendreMonnaieListComp([5000,2000] , 7000))
#2.3
def rendreMonnaie(list , monnaie):
    listRendu = []
    if list == [] :
        listRendu=[0]
        return listRendu
    else:
        for x in list :
            if x == 0:
                listRendu =[0]
                return listRendu
            else:
                n = monnaie / x
            
                listRendu.append(int(n))
                monnaie = (monnaie - x)
            return  listRendu 
            
print(rendreMonnaie([] , 7000))
print(rendreMonnaieRec([5000 , 2000] , 7000))

print(rendreMonnaie([5000 , 2000] , 7000))
print(rendreMonnaieRec([5000 , 3000] , 7000))

#3.1 recursive

def toutRendreMonnaie(list , monnaie):
    toutRendreMonnaie =[]
    if list == [] :
        toutRendreMonnaie.append(0) 
    else:
      toutRendreMonnaie.append(rendreMonnaieRec(list , monnaie))
      return toutRendreMonnaie + [[0] + rendreMonnaieRec(list[1:] , monnaie)]
print(toutRendreMonnaie([5000 , 1000] , 7000))
#3.3
def toutRendreMonnaieItera(list , monnaie):
    toutRendreMonnaie =[]
    l =[]
    if list == [] :
        toutRendreMonnaie=[0]
        return toutRendreMonnaie
    else:
                        
          for x in list : 
                
                    toutRendreMonnaie.append(rendreMonnaie( list[list.index(x):] , monnaie))

          return toutRendreMonnaie
        
print(toutRendreMonnaieItera([5000 , 1000] , 7000))
     
