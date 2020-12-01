from Partie import Partie

class Equipe(Partie):
    def __init__(self, partie, couleur, symbole, compteur=0):
        self.partie = partie
        self.couleur = couleur
        self.compteur = compteur
        self.symbole = symbole
    
    def joue(self):
        '''Fonction qui se charge d'appeller les autres fonctions nécessaires pour faire avancer le jeu'''
        
        self.move()
        print("----------------------------------------------------------")
        self.actualiserCompteur()
        self.partie.gagne(self.compteur, self.couleur)
        


    def demande(self):
        '''Demande à l'utilisateur le pion qu'il veut séléctionné et renvoie deux entiers correspondant a la ligne et a la colonne du pion'''

        print("Aux", self.couleur, "de jouer !")

        #Liste correspondant a toutes les lettres valides lors du choix d'une case
        liste = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        
        while 1:
            #On teste si la lettre entrée se trouve dans liste sinon on redemande une lettre à l'utilisateur
            try:
                lettre = input("Colonne du pion a déplacer (Lettre) : ").upper()
                lettre = liste.index(lettre)
                break

            except:
                print("Cette colonne n'existe pas !")

        #On assigne une valeur a chiffre2 qui rempli les conditions pour rentrer dans la boucle une 1ere fois
        chiffre = -1
        while chiffre < 0 or chiffre > 9:
            #On teste si chiffre2 est un entier sinon on redemande un chiffre à l'utilisateur
            try:
                chiffre = int(input("Ligne du pion a déplacer (Chiffre) : "))

            except ValueError:
                print("Ce n'est pas un chiffre !")

        #Si la case séléctionnée est bien une case où se trouve un de nos pions
        if self.partie.plateau[chiffre][lettre] == self.symbole:
            print("Pion sélectioné")
            return chiffre, lettre

        #Sinon on rappelle la fonction
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
                    #On teste si la lettre entrée se trouve dans liste sinon on redemande une lettre à l'utilisateur
                    try:
                        lettre2 = input("Colonne du déplacement (Lettre) : ").upper()
                        lettre2 = liste.index(lettre2)
                        break

                    except:
                        print("Cette colonne n'existe pas !")
            
                #On assigne une valeur a chiffre2 qui rempli les conditions pour rentrer dans la boucle une 1ere fois
                chiffre2 = -1
                while chiffre2 < 0 or chiffre2 > 9:
                    #On teste si chiffre2 est un entier sinon on redemande un chiffre à l'utilisateur
                    try:
                        chiffre2 = int(input("Ligne du pion a déplacer (Chiffre) : "))
                    except ValueError:
                        print("Ce n'est pas un chiffre !")
                
                #Ces variables sont utilisés lorsqu'un joueur veut effecctuer un saut, elles correspondent à la différence qu'il y a entre la case ou se trouve le pion et la case où le pion veut se rendre
                diffChiffre = int((chiffre2 - chiffre) / 2)
                diffLettre = int((lettre2 - lettre) / 2)

                #On teste si le saut peut être réalisé, si la case est valide
                #Dans cette condition on teste d'abord si la case se trouve bien a la bonne distance pour effectuer un saut à savoir 2 case en diagonale, ensuite on regarde si la case que veut sauter le pion est bien un pion adverse car self.partie.plateau[chiffre + diffChiffre][lettre + diffLettre] correspond en fait à la case que veut sauter le pion (case située entre le pion et là où le pion veut aller)
                if (chiffre2 == chiffre+2 or chiffre2 == chiffre-2 and lettre2 == lettre+2 or lettre2 == lettre-2) and self.partie.plateau[chiffre + diffChiffre][lettre + diffLettre] != "   " and self.partie.plateau[chiffre + diffChiffre][lettre + diffLettre] != self.symbole:
                    
                    #Le pion adverse est supprimé, il est mangé
                    self.partie.plateau[chiffre + diffChiffre][lettre + diffLettre] = "   "

                    #La case séléctionné est valide
                    bonneCaseSelect = True
                    #on actualise notre tableau (on fait bouger le pion sur la case qu'il a choisi)
                    self.partie.plateau[chiffre2][lettre2] = self.symbole
                    self.partie.plateau[chiffre][lettre] = "   "

                else:

                    print("Tu ne peux pas te déplacer ici")
            
            #On revoie la méthode jusqu'à ce que le joueur ne veuille plus sauter
            return self.proposerDoubleSaut()

        elif choix == "n":
            #on appelle la méthode soufflerPasJouer qui renvoie un booléen
            pouvaisSauter = self.soufflerPasJouer(chiffre, lettre)
            
            #Si le joueur pouvait sauter :
            if pouvaisSauter == True:
                print("Tu pouvais sauter !")

        #Si le joueur a entré autre chose que 'o' ou 'n'
        else:
            pouvaisSauter = self.soufflerPasJouer(chiffre, lettre)
            if pouvaisSauter == True:
                print("Tu pouvais sauter !")

    def move(self):
        '''Demande à l'utilisateur la case où il veut déplacer son pion et déplace son pion si la case est valide'''

        #On appelle la méthode demande()
        chiffre, lettre = self.demande()

        liste = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

        #Determine si la case séléctionné est valide
        bonneCaseSelect = False
        #Determine si le joueur est en train de sauter plusieurs fois (double saut, triple saut...)
        enTrainDeSauter = False
        #Détermine si le joueur pouvais sauter (souffler n'est pas joué)
        pouvaisSauter = False

        while not bonneCaseSelect:

            while 1:
                try:
                    lettre2 = input("Colonne du déplacement (Lettre) : ").upper()
                    noMessage = False
                    if lettre2 == "ANNULER":
                        chiffre, lettre = self.demande()
                        noMessage = True
                    lettre2 = liste.index(lettre2)
                    break

                except:
                    if noMessage == False:
                        print("Cette colonne n'existe pas !")
                

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

                #Si le joueur n'essaye pas de sauter (si le joueur essaye d'avancer normalement)
                if diffChiffre < 1 and diffChiffre > -1:
                    if self.couleur == "blancs":
                        #Si les pions blancs vont bien dans le bon sens (car il est impossible de reculer aux dames)
                        if (chiffre2 == chiffre-1) and (lettre2 == lettre+1 or lettre2 == lettre-1):
                            
                            pouvaisSauter = self.soufflerPasJouer(chiffre, lettre)
                            #La case est valide on peux sortir de la boucle
                            bonneCaseSelect = True
                        else:
                            print("Vous ne pouvez pas aller en arrière")

                    elif self.couleur == "noirs":
                        if (chiffre2 == chiffre+1) and (lettre2 == lettre+1 or lettre2 == lettre-1):

                            pouvaisSauter = self.soufflerPasJouer(chiffre, lettre)

                            bonneCaseSelect = True
                        else:
                            print("Vous ne pouvez pas aller en arrière")

                #Pareil que pour la méthode proposerDoubleSaut()
                elif (chiffre2 == chiffre+2 or chiffre2 == chiffre-2 and lettre2 == lettre+2 or lettre2 == lettre-2) and self.partie.plateau[chiffre + diffChiffre][lettre + diffLettre] != "   " and self.partie.plateau[chiffre + diffChiffre][lettre + diffLettre] != self.symbole:
                    
                    self.partie.plateau[chiffre + diffChiffre][lettre + diffLettre] = "   "
                    bonneCaseSelect = True
                    enTrainDeSauter = True


                else:
                    print("Vous ne pouvez pas aller sur cette case !")

        #Si le joueur pouvais sauter (le seul probleme c'est que ca marche que si c'est le pion séléctionné qui n'a pas sauté)
        if pouvaisSauter:
            self.partie.plateau[chiffre][lettre] = "   "
            print("Ton pion est supprimé")


        else:
            #On actualise le tableau (on fait bouger notre pion)
            self.partie.plateau[chiffre2][lettre2] = self.symbole
            self.partie.plateau[chiffre][lettre] = "   "

        #Si le joueur a déjà sauter on lui propose de resauter
        if enTrainDeSauter:
            self.proposerDoubleSaut(chiffre2, lettre2)

    def soufflerPasJouer(self, chiffre, lettre):
        '''Vérifie si le joueur pouvais sauter, si oui : souffler n'est pas joué'''
        
        if (self.partie.plateau[chiffre+1][lettre+1] != self.symbole and self.partie.plateau[chiffre+1][lettre+1] != "   ") and self.partie.plateau[chiffre+2][lettre+2] == "   ":
            print("Tu pouvais sauter")
            return True
        
        elif (self.partie.plateau[chiffre+1][lettre-1] != self.symbole and self.partie.plateau[chiffre+1][lettre-1] != "   ") and self.partie.plateau[chiffre+2][lettre-2] == "   ":
            print("Tu pouvais sauter")
            return True
        
        elif (self.partie.plateau[chiffre-1][lettre+1] != self.symbole and self.partie.plateau[chiffre-1][lettre+1] != "   ") and self.partie.plateau[chiffre-2][lettre+2] == "   ":
            print("Tu pouvais sauter")
            return True
        
        elif (self.partie.plateau[chiffre-1][lettre-1] != self.symbole and self.partie.plateau[chiffre-1][lettre-1] != "   ") and self.partie.plateau[chiffre-2][lettre-2] == "   ":
            print("Tu pouvais sauter")
            return True

        return False

    def actualiserCompteur(self):
        '''Actualise le compteur'''
        #Compte le nombre de pion dans la grille et actualise le compteur
        for elt in self.partie.plateau:
            for sousElt in elt:
                if sousElt != self.symbole and sousElt != "   ":
                    self.compteur += 1
        
        self.compteur = 20 - self.compteur