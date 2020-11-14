from Partie import Partie
import replit

class Equipe(Partie):
    def __init__(self, partie, couleur, symbole, compteur=0):
        self.partie = partie
        self.couleur = couleur
        self.compteur = compteur
        self.symbole = symbole
    
    def joue(self):
        
        self.move()
        replit.clear()
        


    def demande(self):
        '''Demande à l'utilisateur la case du pion qu'il veut déplacer et renvoie deux entiers'''

        liste = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        
        while 1:
            try:
                lettre = input("Colonne du pion a déplacer (Lettre) : ").upper()
                lettre = liste.index(lettre)
                break

            except:
                print("Cette colonne n'existe pas !")

        chiffre = -1
        while chiffre < 0 or chiffre > 9:

            try:
                chiffre = int(input("Ligne du pion a déplacer (Chiffre) : "))

            except ValueError:
                print("Ce n'est pas un chiffre !")

        if self.partie.plateau[chiffre][lettre] == self.symbole:
            print("Pion sélectioné")
            return chiffre, lettre

        else:
            print("Tu n'as pas de pion a cette case !")
            return self.demande()


    # def saut(self):

    def move(self):
        '''Demande à l'utilisateur la case où il veut déplacer son pion'''

        chiffre, lettre = self.demande()

        liste = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

        bonneCaseSelect = False

        while not bonneCaseSelect:

            while 1:
                try:
                    lettre2 = input("Colonne du déplacement (Lettre) : ").upper()
                    lettre2 = liste.index(lettre2)
                    break

                except:
                    print("Cette colonne n'existe pas !")

            chiffre2 = -1
            while chiffre2 < 0 or chiffre2 > 9:
                try:
                    chiffre2 = int(input("Ligne du pion a déplacer (Chiffre) : "))
                except ValueError:
                    print("Ce n'est pas un chiffre !")


            if self.partie.plateau[chiffre2][lettre2] !=  "   ":
                print("Cette case n'est pas vide !")
            else:
                diffChiffre = int((chiffre2 - chiffre) / 2)
                diffLettre = int((lettre2 - lettre) / 2)

                if (chiffre2 == chiffre+1 or chiffre2 == chiffre-1) and (lettre2 == lettre+1 or lettre2 == lettre-1):

                    bonneCaseSelect = True

                elif (chiffre2 == chiffre+2 or chiffre2 == chiffre-2 and lettre2 == lettre+2 or lettre2 == lettre-2) and self.partie.plateau[chiffre + diffChiffre][lettre + diffLettre] != "   " and self.partie.plateau[chiffre + diffChiffre][lettre + diffLettre] != self.symbole:

                    self.partie.plateau[chiffre + diffChiffre][lettre + diffLettre] = "   "
                    self.compteur += 1
                    bonneCaseSelect = True


                else:
                    
                    print("NONNONNONON")
                    print(chiffre, lettre)
                    print(chiffre2, lettre2)


        self.partie.plateau[chiffre2][lettre2] = self.symbole
        self.partie.plateau[chiffre][lettre] = "   "
        
            