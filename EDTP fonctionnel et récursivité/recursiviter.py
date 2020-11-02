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
            return list3 + list2 + list[1:]
        elif nb < list[0] :
            list2 = [nb]
            return list2 + list
#5
NewList = []
def trierList(list):
    if list == [] :
        return list
    elif len(list) == 1 :
        return list
    elif list[0] > list[1] :
      for x in list:
          if list[0] > x:
            print(x)
    #   NewList = [list[1],list[0]] 
    #   return NewList + trierList(list[2:])
    else:
        return list[0]+trierList(list[1:])

if __name__ == "__main__":
    list = [ 3, 1, 2, 0, 4]
    print(nbElement(list))
    print(sommeElement(list))
    print(moyenneElement(list))
    print(trierList([5, 4 ,1 ,0 ,2]))
    print(insereElement_ListTrier([ 1, 3, 4, 5] , 2))
