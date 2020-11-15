from Equipe import Equipe, Partie, replit

partie = Partie()

noir = Equipe(partie, "noirs", " o ", 19)
blanc = Equipe(partie, "blancs", " ● ")

partie.regles()
commencerJeu = input("Appuyez sur entrée pour commencer !")
replit.clear()

while not partie.fin:
    partie.affiche(noir.compteur, blanc.compteur)
    blanc.joue()
    
    if not partie.fin:
        partie.affiche(noir.compteur, blanc.compteur)
        noir.joue()
        
    else:
        break
