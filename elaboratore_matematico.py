from main import GestoreMatrice

class ElaboratoreMatematico(GestoreMatrice):
    
    def trasponi(self):
        matriceTrasp = [
    [riga[i] for riga in self.matrice] 
                
                for i in range(len(self.matrice))  ] 
        return matriceTrasp
    
    def moltiplica_per_scalare(self, k):
         
            for i in range(len(self.matrice)):
                for j in range(len(self.matrice[i])):
                    self.matrice[i][j] = k * self.matrice[i][j] 
                    
            return self.matrice

matrice1=[[1,2,3],[3,3,3],[1,2,3]]         
matrice = ElaboratoreMatematico(matrice1)
print(matrice.moltiplica_per_scalare(2))