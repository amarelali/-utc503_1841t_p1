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
# NewList = []
# def trierList(list):
#     if list[0] > list[1] :
#         NewList.append(list[1])
#         NewList.append(list[0])
#     else:
#         return list[0]+trierList(list[1:])



if __name__ == "__main__":
    list = [ 3, 1, 2, 0, 4]
    print(nbElement(list))
    print(sommeElement(list))
    print(moyenneElement(list))
    # print(trierList(list))
