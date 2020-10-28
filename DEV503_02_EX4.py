import decomposer
class Fraction:

    def __init__(self,num,deno):
        self.num = num
        self.deno = deno

    def show(self):
        print(self.num,"/",self.deno)
    def __add__(self,secondfraction):

        newnum = self.num * secondfraction.deno + self.deno * secondfraction.num
        newden = self.deno * secondfraction.deno

        return Fraction(newnum,newden)
    def __mult__(self,secondfraction):

        newnum = self.num * secondfraction.num 
        newden = self.deno * secondfraction.deno

        return Fraction(newnum,newden)
def removeCommonElements(a, b):
    for e in a[:]:
        if e in b:
            a.remove(e)
            b.remove(e)

def simplifier(fraction):
    num = 1
    demo = 1
    listNum = decomposer.decompose(fraction.num)
    listDemo = decomposer.decompose(fraction.deno)
    
    removeCommonElements(listNum , listDemo)

    for i in listNum:
        num *=i
    for i in listDemo:
        demo *=i
    return Fraction(num,demo)

def main():
    f1 = Fraction(3,5)
    f2 = Fraction(8,4)
    f1.show()
    f2.show()
    f3 = f1 + f2
    f3.show()
    f4 = simplifier(f3)
    f4.show()
    f5 = Fraction(3,5)
    f6 = Fraction(8,4)
    f7 = f5.__mult__(f6)
    f7.show()
    f8 = simplifier(f7)
    f8.show()

if __name__ == "__main__":
    main() 