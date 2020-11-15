class Partie:
    def __init__(self, plateau=[["   ", " o ", "   ", " o ", "   ", " o ", "   ", " o ", "   ", " o "], [" o ", "   ", " o ", "   ", " o ", "   ", " o ", "   ", " o ", "   "], ["   ", " o ", "   ", " o ", "   ", " o ", "   ", " o ", "   ", " o "], [" o ", "   ", " o ", "   ", " o ", "   ", " o ", "   ", " o ", "   "], ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "], ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "], ["   ", " ● ", "   ", " ● ", "   ", " ● ", "   ", " ● ", "   ", " ● "], [" ● ", "   ", " ● ", "   ", " ● ", "   ", " ● ", "   ", " ● ", "   "], ["   ", " ● ", "   ", " ● ", "   ", " ● ", "   ", " ● ", "   ", " ● "], [" ● ", "   ", " ● ", "   ", " ● ", "   ", " ● ", "   ", " ● ", "   "]], fin=False):
        self.plateau = plateau
        self.fin = fin

    def affiche(self, compteur1, compteur2):
        
        print("    A   B   C   D   E   F   G   H   I   J  ")
        for i in range(len(self.plateau)):
            print("  -----------------------------------------  ", end="")
            if i == 0:
                print(compteur2, end="")
            print("")
            print(i, " ", end="", sep="")
            for j in range(len(self.plateau[i])):
                print('|'+self.plateau[i][j], end="")
    
            print("|")
        print("  -----------------------------------------  ", compteur1)                                                                                                                                                                  

    def regles(self):

        print("Voici les règles principales du jeu de dames:\n- L'objectif est de manger tous les pions de votre adversaire.\nPour cela, vous devez passer au-dessus d'un pion adverse, à condition que la case sur laquelle vous arrivez est libre.\n- Vous déplacez vos pions chacun votre tour, en diagonale seulement.\n- N'oubliez pas la règle du <<souffler n'est pas joué>> : si vous pouvez prendre un pion, vous DEVEZ le prendre.\nBonne chance ! ")
        print("----------------------------------------------------------")

    def gagne(self, compteur):

        if compteur >= 20:

            self.fin = True
            print("aaaaaa")