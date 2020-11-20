from Partie import Partie
import replit

class Equipe(Partie):
    def __init__(self, partie, couleur, symbole, compteur=0):
        self.partie = partie
        self.couleur = couleur
        self.compteur = compteur
        self.symbole = symbole
    
    def joue(self):
        '''Fonction qui se charge d'appeller les autres fonctions nécessaires pour faire avancer le jeu'''
        
        self.move()
        self.partie.gagne(self.compteur, self.couleur)
        


    def demande(self):
        '''Demande à l'utilisateur le pion qu'il veut séléctionné et renvoie deux entiers correspondant a la ligne et a la colonne du pion'''

        print("Aux", self.couleur, "de jouer !")

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


    def proposerDoubleSaut(self, chiffre, lettre):
        '''Fonction qui demande au joueur si il souhaite sauter plusieurs pions d'un coup tant que le joueur peux sauter'''

        choix = input('Pensez vous pouvoir continuer a sauter ? (o/n)').lower()
        print(choix)

        if choix == "o":
            
            #Liste correspondant a toutes les lettres valides lors du choix d'une case
            liste = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

            #On initialise la variable a False pour rentrer dans la boucle une 1ere fois
            bonneCaseSelect = False

            #Tant que la case séléctionée n'est pas valide:
            while not bonneCaseSelect:

                while 1:
                    try:
                        #On teste si la lettre entrée se trouve dans liste sinon on redemande une lettre à l'utilisateur
                        lettre2 = input("Colonne du déplacement (Lettre) : ").upper()
                        lettre2 = liste.index(lettre2)
                        break

                    except:
                        print("Cette colonne n'existe pas !")
            
                #On assigne une valeur a chiffre2 qui rempli les conditions pour rentrer dans la boucle une 1ere fois
                chiffre2 = -1
                while chiffre2 < 0 or chiffre2 > 9:
                    try:
                        #On teste si chiffre2 est un entier sinon on redemande un chiffre à l'utilisateur
                        chiffre2 = int(input("Ligne du pion a déplacer (Chiffre) : "))
                    except ValueError:
                        print("Ce n'est pas un chiffre !")
                
                #Ces variables sont utilisés lorsqu'un joueur veut effecctuer un saut, elles correspondent à la différence qu'il y a entre la case ou se trouve le pion et la case où le pion veut se rendre
                diffChiffre = int((chiffre2 - chiffre) / 2)
                diffLettre = int((lettre2 - lettre) / 2)

                #On teste si le saut peut être réalisé, si la case est valide
                if (chiffre2 == chiffre+2 or chiffre2 == chiffre-2 and lettre2 == lettre+2 or lettre2 == lettre-2) and self.partie.plateau[chiffre + diffChiffre][lettre + diffLettre] != "   " and self.partie.plateau[chiffre + diffChiffre][lettre + diffLettre] != self.symbole:
                    
                    self.partie.plateau[chiffre + diffChiffre][lettre + diffLettre] = "   "
                    self.compteur += 1
                    bonneCaseSelect = True
                    self.partie.plateau[chiffre2][lettre2] = self.symbole
                    self.partie.plateau[chiffre][lettre] = "   "

                else:

                    print("Tu ne peux pas te déplacer ici")
            
            return self.proposerDoubleSaut()

        elif choix == "n":

            pouvaisSauter = self.soufflerPasJouer(chiffre, lettre)

            if pouvaisSauter == True:
                print("Tu pouvais sauter !")
        else:
            pouvaisSauter = self.soufflerPasJouer(chiffre, lettre)
            if pouvaisSauter == True:
                print("Tu pouvais sauter !")

    def move(self):
        '''Demande à l'utilisateur la case où il veut déplacer son pion'''

        chiffre, lettre = self.demande()

        liste = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

        bonneCaseSelect = False
        enTrainDeSauter = False
        pouvaisSauter = False

        while not bonneCaseSelect:

            while 1:
                try:
                    lettre2 = input("Colonne du déplacement (Lettre) : ").upper()
                    lettre2 = liste.index(lettre2)
                    break

                except:
                    print("Cette colonne n'existe pas !")

            #On assigne une valeur a chiffre2 pour rentrer dans la boucle une 1ere fois
            chiffre2 = -1
            while chiffre2 < 0 or chiffre2 > 9:
                try:
                    chiffre2 = int(input("Ligne du déplacement (Chiffre) : "))
                except ValueError:
                    print("Ce n'est pas un chiffre !")


            if self.partie.plateau[chiffre2][lettre2] !=  "   ":
                print("Cette case n'est pas vide !")

            else:

                diffChiffre = int((chiffre2 - chiffre) / 2)
                diffLettre = int((lettre2 - lettre) / 2)

                if self.couleur == "blancs":
                    if (chiffre2 == chiffre-1) and (lettre2 == lettre+1 or lettre2 == lettre-1):

                        pouvaisSauter = self.soufflerPasJouer(chiffre, lettre)
                        if pouvaisSauter == True:
                            print("Tu pouvais sauter !")

                        bonneCaseSelect = True
                    else:
                        print("Vous ne pouvez pas aller en arrière")

                elif self.couleur == "noirs":
                    if (chiffre2 == chiffre+1) and (lettre2 == lettre+1 or lettre2 == lettre-1):

                        pouvaisSauter = self.soufflerPasJouer(chiffre, lettre)
                        if pouvaisSauter == True:
                            print("Tu pouvais sauter !")

                        bonneCaseSelect = True
                    else:
                        print("Vous ne pouvez pas aller en arrière")

                elif (chiffre2 == chiffre+2 or chiffre2 == chiffre-2 and lettre2 == lettre+2 or lettre2 == lettre-2) and self.partie.plateau[chiffre + diffChiffre][lettre + diffLettre] != "   " and self.partie.plateau[chiffre + diffChiffre][lettre + diffLettre] != self.symbole:

                    self.partie.plateau[chiffre + diffChiffre][lettre + diffLettre] = "   "
                    self.compteur += 1
                    bonneCaseSelect = True
                    enTrainDeSauter = True


                else:
                    
                    print("Vous ne pouvez pas aller sur cette case !")

        if pouvaisSauter:
            self.partie.plateau[chiffre][lettre] = "   "
            self.partie.compteurARetenir = 1


        else:
            self.partie.plateau[chiffre2][lettre2] = self.symbole
            self.partie.plateau[chiffre][lettre] = "   "

        if enTrainDeSauter:
            self.proposerDoubleSaut(chiffre2, lettre2)

    def soufflerPasJouer(self, chiffre, lettre):
        
            if (self.partie.plateau[chiffre+1][lettre+1] != self.symbole and self.partie.plateau[chiffre+1][lettre+1] != "   ") and self.partie.plateau[chiffre+2][lettre+2] == "   ":
                print("Tu pouvais sauter")
            
            elif (self.partie.plateau[chiffre+1][lettre-1] != self.symbole and self.partie.plateau[chiffre+1][lettre-1] != "   ") and self.partie.plateau[chiffre+2][lettre-2] == "   ":
                print("Tu pouvais sauter")
            
            elif (self.partie.plateau[chiffre-1][lettre+1] != self.symbole and self.partie.plateau[chiffre-1][lettre+1] != "   ") and self.partie.plateau[chiffre-2][lettre+2] == "   ":
                print("Tu pouvais sauter")
            
            elif (self.partie.plateau[chiffre-1][lettre-1] != self.symbole and self.partie.plateau[chiffre-1][lettre-1] != "   ") and self.partie.plateau[chiffre-2][lettre-2] == "   ":
                print("Tu pouvais sauter")