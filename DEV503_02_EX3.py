class Monnaie:
    def __init__(self, valeur, devise):
        self.valeur = valeur
        self.devise = devise

    def ajoutMonnaie(self, monnaie): 
        if self.devise  == monnaie.devise: 
            self.valeur = self.valeur + monnaie.valeur
        else:
             print("il faut ajouter monnaies de meme devise")
    def retrancheMonnaie(self, monnaie): 
        if self.devise  == monnaie.devise: 
            
            self.valeur =  self.valeur - monnaie.valeur   
        else:
            print("il faut ajouter monnaies de meme devise")
def main():
    m1 = Monnaie(5,"euros")
    m2 = Monnaie(7,"euros") 

    print("apres l'ajout ")
    m1.ajoutMonnaie(m2)
    print(m1.valeur)
    
    m1.valeur = 5
    m1.retrancheMonnaie(m2)
    print("apres retranche")
    print(m1.valeur)
if __name__ == "__main__":
    main() 
