from Equipe import Equipe, Partie, replit

partie = Partie()

noir = Equipe(partie, "noir", " ● ", 19)
blanc = Equipe(partie, "blanc", " o ")

partie.regles()
commencerJeu = input("Appuyez sur entrée pour commencer !")
replit.clear()
partie.affiche(noir.compteur, blanc.compteur)

while not partie.fin:
    noir.joue()
    partie.affiche(noir.compteur, blanc.compteur)
    if not partie.fin:
        blanc.joue()
        partie.affiche(noir.compteur, blanc.compteur)
    else:
        break
