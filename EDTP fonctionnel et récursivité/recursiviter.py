tete_ = lambda l : l[0]
reste_= lambda l : l[1:]
# 1
def nbElement(list):
    if list == [] :
        return 0
    else:
        return 1 + nbElement(reste_(list)) 
# 2
def sommeElement(list):
    if list == [] :
        return 0
    else:
        return tete_(list) + sommeElement(reste_(list)) 
# 3
def moyenneElement(list):
    if len(list) == 1 :
        return tete_(list)
    else:
        return (tete_(list) + (len(list) - 1) * moyenneElement(reste_(list))) / len(list)
#4
def insereElement_ListTrier(list , nb):
    if len(list) == 1 :
        return tete_(list)
    else:
        if nb > list[0]:
            list2 = [nb]
            list3 = [list[0]]
            return list3 + list2 + reste_(list)
        elif nb < list[0] :
            list2 = [nb]
            return list2 + list
#5 
def partition(L,debut,fin):
    pivot = L[fin]
    i = debut
    j = debut
    while j < fin:
        if L[j] <= pivot:
            L[i],L[j] = L[j],L[i]
            i += 1
        j += 1
    L[fin],L[i] = L[i],L[fin]
    return i
def tri_partition_recursif(L,debut,fin):
    if debut < fin:
        i = partition(L,debut,fin)
        tri_partition_recursif(L,debut,i-1)
        tri_partition_recursif(L,i+1,fin)
                    
def tri_partition(liste):
    L =  liste
    tri_partition_recursif(L,0,len(L)-1)
    return L
#6
def rendreMonnaieRec(list , monnaie):
    listRendu = []
    if list == [] :
         return listRendu
    else:            
            n = monnaie / list[0]
            listRendu.append(int(n))

            monnaie = (monnaie - list[0])
            return listRendu + rendreMonnaieRec(list[1:] , monnaie)              
if __name__ == "__main__":
    list = [ 3, 1, 2, 0, 4]
    print(nbElement(list))
    print(sommeElement(list))
    print(moyenneElement(list))
    print(tri_partition([5, 4 ,1 ,0 ,2]))
    print(insereElement_ListTrier([ 1, 3, 4, 5] , 2))
    print(rendreMonnaieRec([5000 , 1000] , 7000))