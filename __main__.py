class GestoreMatrice:
    def __init__(self,matrice: list[list]):
        self.matrice=matrice
    def stampa_matrice(self):
        for righe in self.matrice:
            print(righe)
    
    def valida_matrice(self):
        if len(self.matrice)==1:
            return True
        for i in range(len(self.matrice)-1):
            if len(self.matrice[i])!=len(self.matrice[i+1]):
                return False
        return True




matrice1=[[1,2,3],[3,3,3],[1,2,3]]  
matrice=GestoreMatrice([[1,2,3],[3,3,3],[1,2,3],[1,2,5,6]])        
matrice.stampa_matrice()
valid=matrice.valida_matrice()
print(valid)

class ElaboratoreStatistico(GestoreMatrice):
    def __init__(self, matrice):
        GestoreMatrice.__init__(self,matrice)
    def trova_massimo(self):
        return max(max(self.matrice))
    def media_riga(self,indice_riga):
        n=len(self.matrice[indice_riga])
        return sum(self.matrice[indice_riga])/n

matrice=ElaboratoreStatistico([[1,2,3],[3,3,3],[1,2,3],[1,2,5,6]])        
print(matrice.trova_massimo())
print(matrice.media_riga(1))


