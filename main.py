#il y a encore quelques bugs que nous n'avons pas réussi à gérer ou que nous ne comprenons pas mais nous avons fait de notre mieux, il faut que vous essayez de ne pas vous tromper dans les mouvement que vous voulez réaliser (notamment lors d'un saut) car cela peux causer des bugs meme si c'est très rare

from Equipe import Equipe, Partie

#Instance de la classe Partie
partie = Partie()

#2 instances de la classe Equipe qui  vont représenter les pions noir et blanc
noir = Equipe(partie, "noirs", " o ")
blanc = Equipe(partie, "blancs", " ● ")

#On affiche les règles au début
partie.regles()
#On attend que l'utilisateur appuie sur entrée pour executer la suite du programme
commencerJeu = input("Appuyez sur entrée pour commencer !")
print("----------------------------------------------------------")

#Tant que partie.fin == False ou tant que la partie n'est pas finie
while not partie.fin:
    #On affiche la grille (on le fait ici car on ne peut pas le faire dans la méthode joue)
    partie.affiche(noir.compteur, blanc.compteur)
    #On appelle la méthode joue
    blanc.joue()
    
    #On regarde si notre partie.fin n'a pas changé entre temps
    if not partie.fin:

        partie.affiche(noir.compteur, blanc.compteur)
        noir.joue()
    
    #Si la partie est finie
    else:
        #On quitte la boucle
        break