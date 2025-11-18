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







