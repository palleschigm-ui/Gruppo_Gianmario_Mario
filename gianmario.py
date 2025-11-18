import main 
class ElaboratoreStatistico(main.GestoreMatrice):
    def __init__(self, matrice):
        main.GestoreMatrice.__init__(self,matrice)
    def trova_massimo(self):
        return max(max(self.matrice))
    def media_riga(self,indice_riga):
        n=len(self.matrice[indice_riga])
        return sum(self.matrice[indice_riga])/n
